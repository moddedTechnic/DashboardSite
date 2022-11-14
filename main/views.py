from django.apps import apps
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static


def index(request: HttpRequest) -> HttpResponse:
    """Serves the index page"""
    return render(
        request, 'index.html', {
            'title': 'Dashboard',
        }
    )


def favicon(request: HttpRequest) -> HttpResponse:
    """Serves the favicon"""
    return HttpResponseRedirect(static('img/logo.ico'))
