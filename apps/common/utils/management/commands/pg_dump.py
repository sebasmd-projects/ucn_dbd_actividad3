import os
import subprocess
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a PostgreSQL database schema dump for dbdiagram.io'

    def add_arguments(self, parser):
        parser.add_argument(
            '-pv',
            '--pversion',
            default='16',
            help='PostgreSQL version'
        )
        parser.add_argument(
            '--host',
            default='localhost',
            help='PostgreSQL host'
        )
        parser.add_argument(
            '--port',
            default='5432',
            help='PostgreSQL port'
        )

    def handle(self, *args, **options):
        postgres_version = options["pversion"]
        host = options["host"]
        port = options["port"]

        nombredb = settings.DATABASES['default']['NAME']
        userdb = settings.DATABASES['default']['USER']
        
        timestamp = datetime.now().strftime('%d/%m/%Y %I:%M %p')

        # Step 1: Change directory to PostgreSQL bin directory
        os.chdir(f"C:\\Program Files\\PostgreSQL\\{postgres_version}\\bin")

        # Step 2: Run pg_dump command
        dump_file = os.path.join(
            settings.BASE_DIR, settings.UTILS_DATA_PATH, "database_schema.sql"
        )
        dump_command = [
            "pg_dump",
            "-h", host,
            "-p", port,
            "-d", nombredb,
            "-U", userdb,
            "-s",
            "-F", "p",
            "-E", "UTF-8",
            "-f", dump_file
        ]

        self.stdout.write(
            f'{self.style.SUCCESS("DB User:")} {userdb}'
        )

        try:
            subprocess.run(dump_command)
            
            with open(dump_file, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(f'-- {timestamp}\n' + content)
            
            self.stdout.write(
                '{} {}'.format(self.style.SUCCESS(
                    "Database schema dumped successfully to:"), os.path.abspath(dump_file))
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f'Cannot create postgresql schema, error: {e}'
                )
            )
