from pathlib import Path

from .settings_apps import CUSTOM_APPS

BASE_DIR = Path(__file__).resolve().parent.parent.parent


LOCALE_PATHS = [
    app_path / 'locale' for app_path in [BASE_DIR / app.replace('.', '/') for app in CUSTOM_APPS]
]

LOCALE_PATHS.append(str(BASE_DIR / 'app_core' / 'locale'))
