from django.shortcuts import render
from django.template.context import RequestContext


def pageNotFound(request, exception):
    response = render(None, '404.html', RequestContext(request))
    response.status_code = 404
    return response