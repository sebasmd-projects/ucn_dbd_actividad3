import json
import logging
import os
from getpass import getpass
from logging import Logger

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

logger: Logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create, add, delete, or remove superusers from JSON and/or database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-a', '--add', action='store_true',
            help='Add a new user to the JSON file'
        )
        parser.add_argument(
            '-ac', '--addcreate', action='store_true',
            help='Add a new user to the JSON file and DB'
        )
        parser.add_argument(
            '-as', '--addsuperuser', action='store_true',
            help='Add a new superuser to the JSON file'
        )
        parser.add_argument(
            '-acs', '--addcreatesuperuser', action='store_true',
            help='Add a new superuser to the JSON file and DB'
        )
        parser.add_argument(
            '-d', '--delete', action='store_true',
            help='Delete an existing user from JSON file'
        )
        parser.add_argument(
            '-dr', '--deleteremove', action='store_true',
            help='Delete an existing user from JSON file and DB'
        )

    def handle(self, *args, **options):
        utils_data_path: str = getattr(settings, 'UTILS_DATA_PATH', None)

        user_data_file = os.path.join(utils_data_path, 'users.json')

        if options['add'] or options['addsuperuser']:
            is_superuser = True if options['addsuperuser'] else False
            new_user = self.request_user_data()
            self.add_user(user_data_file, is_superuser, new_user)

        elif options['addcreate'] or options['addcreatesuperuser']:
            is_superuser = True if options['addcreatesuperuser'] else False
            new_user = self.request_user_data()
            self.add_user(user_data_file, is_superuser, new_user)
            self.add_create_user(is_superuser, new_user)

        elif options['delete']:
            self.delete_user(user_data_file, False)

        elif options['deleteremove']:
            self.delete_user(user_data_file, True)

        else:
            User = get_user_model()
            existing_users = self.get_existing_users(user_data_file)

            for user_data in existing_users:
                username = user_data["username"]
                email = user_data["email"]
                first_name = user_data["first_name"]
                last_name = user_data["last_name"]
                password = user_data["password"]
                is_superuser = user_data["is_superuser"] in ['Yes', 'yes', 'si', 'Si']
                
                if not User.objects.filter(username=username).exists() and is_superuser:
                    with transaction.atomic():
                        try:
                            User.objects.create_superuser(
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                password=password
                            )
                            logger.warning(
                                f'Super user created | {username}'
                            )
                        except Exception as e:
                            logger.error(
                                f'Super user {username}: \n{e}'
                            )
                else:
                    with transaction.atomic():
                        try:
                            User.objects.create_user(
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                password=password
                            )
                            logger.warning(
                                f'User created | {username}'
                            )
                        except Exception as e:
                            logger.error(
                                f'User {username}: \n{e}'
                            )

    def get_existing_users(self, user_data_file):
        try:
            with open(user_data_file, 'r') as json_file:
                existing_users = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            existing_users = []

        return existing_users

    def request_user_data(self):
        username = input('Enter username: ')
        email = input('Enter email: ')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        password = getpass('Enter password: ')
        confirm_password = getpass('Confirm password: ')

        while password != confirm_password:
            self.stdout.write(
                self.style.WARNING(
                    'Password does not match!'
                )
            )
            password = getpass('Enter password:')
            confirm_password = getpass('Confirm password:')

        return username, email, first_name, last_name, password

    def request_user_to_delete(self):
        return input('Enter username or email to delete: ')

    def add_user(self, user_data_file, is_superuser, new_user):
        username, email, first_name, last_name, password = new_user
        user_dont_exists = True
        existing_users = self.get_existing_users(user_data_file)

        for user in existing_users:
            if user["username"] == username or user["email"] == email:
                user_dont_exists = False
                break

        if user_dont_exists:
            existing_users.append({
                "username": username,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
                "is_superuser": 'Yes' if is_superuser else 'No'
            })

            with open(user_data_file, 'w') as json_file:
                json.dump(existing_users, json_file, indent=4)

            logger.warning(
                f'{"Super user" if is_superuser else "user"} added to json | {username}'
            )
        else:
            logger.error(
                f'{"Super user" if is_superuser else "user"} couldnt be added to json | {username}'
            )

    def add_create_user(self, is_superuser, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username=kwargs['username']).exists() or not User.objects.filter(email=kwargs['email']).exists():
            if is_superuser:
                with transaction.atomic():
                    User.objects.create_superuser(
                        username=kwargs['username'],
                        email=kwargs['email'],
                        first_name=kwargs['first_name'],
                        last_name=kwargs['last_name'],
                        password=kwargs['password']
                    )
            else:
                with transaction.atomic():
                    User.objects.create_user(
                        username=kwargs['username'],
                        email=kwargs['email'],
                        first_name=kwargs['first_name'],
                        last_name=kwargs['last_name'],
                        password=kwargs['password']
                    )
            logger.warning(
                f'{"Super user" if is_superuser else "user"} created | {kwargs['username']}'
            )
        else:
            logger.error(
                f'{"Super user" if is_superuser else "user"} could not be created | {kwargs['username']}'
            )

    def delete_user(self, user_data_file, remove):
        User = get_user_model()
        user_to_delete = self.request_user_to_delete()
        existing_users = self.get_existing_users(user_data_file)

        user_dont_exists = True

        for user in existing_users:
            if ('@' in user_to_delete and user['email'] == user_to_delete) or (user['username'] == user_to_delete):
                existing_users.remove(user)
                break

        if remove:
            try:
                if '@' in user_to_delete:
                    user = User.objects.get(
                        email=user_to_delete
                    )
                else:
                    user = User.objects.get(
                        username=user_to_delete
                    )
                user.delete()
                user_dont_exists = False
            except User.DoesNotExist:
                logger.error(f'User {user_to_delete} does not exist in DB')

        with open(user_data_file, 'w') as json_file:
            json.dump(existing_users, json_file, indent=4)

        if user_dont_exists:
            logger.error(
                f'{user_to_delete} does not exist in JSON file'
            )
        else:
            logger.warning(
                f'{user_to_delete} removed from JSON file'
            )
