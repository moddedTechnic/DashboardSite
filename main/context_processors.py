from django.apps import apps
from django.conf import settings
from django.http import HttpRequest

from main.apps import MainConfig


def current_app(request: HttpRequest) -> dict:
    path_parts = request.path.split('/')
    return {
        'current_app': path_parts[1] if len(path_parts) > 1 and path_parts[1] else 'main'
    }


def title(request: HttpRequest) -> dict:
    for app in apps.get_app_configs():
        if not hasattr(app, 'base_path'):
            continue
        if app.base_path == current_app(request):
            return {'title': app.verbose_name}
    return {'title': 'Dashboard'}


def widget_apps(request: HttpRequest) -> dict:
    return {
        'apps': [app for app in apps.get_app_configs() if hasattr(app, 'widgets') and not isinstance(app, MainConfig)]
    }
