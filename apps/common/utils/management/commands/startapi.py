import os

from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a custom Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory. "
        "ejm: python manage.py startapi <app_name> <directory/app_name>"
    )

    missing_args_message = "You must provide an application name. \npython manage.py startapi <app_name> <directory/app_name>"

    def handle(self, **options):
        def make_file_path(path, *paths):
            return os.path.join(path, *paths)

        def file_path(file, target=False):
            if target:
                directory = make_file_path(target, file)
            else:
                directory = make_file_path(file)
            return directory

        app_name:str = options.pop("name")
        target = options.pop("directory")

        if target and not os.path.exists(target):
            os.makedirs(f"{target}")

        # Create app structure using Django's template command
        super().handle("app", app_name, target, **options)

        # Create 'api' directory and its contents
        api_directory = file_path('api', target)
        os.makedirs(api_directory)
        
        # Create 'README.md' file and content
        readme_content = f"# {app_name.upper()}"
        readme_content += f'\n\n## Description\n'
        with open(make_file_path(target, 'README.md'), 'w') as readme_file:
            readme_file.write(readme_content)
        
        # Create files for api directory
        api_files = ['__init__.py', 'serializers.py', 'views.py']
        for file in api_files:
            open(make_file_path(api_directory, file), 'a').close()

        # Create urls file in api directory
        urls_content = "from django.urls import include, path\n\nurlpatterns = []"
        with open(make_file_path(api_directory, 'urls.py'), 'w') as urls_file:
            urls_file.write(urls_content)

        # Edit apps.py
        apps_py_path = file_path('apps.py', target)
        if target:
            apps_py_content = f"    name = '{target.replace('/', '.')}'"
        else:
            apps_py_content = f"    name = '{app_name}'"

        with open(apps_py_path, 'r') as apps_py_file:
            existing_content = apps_py_file.readlines()

        existing_content[5] = apps_py_content + '\n'

        with open(apps_py_path, 'w') as apps_py_file:
            apps_py_file.writelines(existing_content)

        # Update the main app's urls.py to include the api_urls
        main_urls_path = file_path('urls.py', target)
        main_urls_content = "from django.urls import include, path\nfrom .api import urls as api_urls\nurlpatterns = []"
        with open(main_urls_path, 'a') as main_urls_file:
            main_urls_file.write(main_urls_content)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created app: {app_name}'
            )
        )
