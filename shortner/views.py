from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Link
from random import randint


def index(request):
    return render(request, 'index.html', {})


def redirect(request, prefix):
    link = Link.objects.filter(prefix__exact=str(prefix)).last()
    if not(link):
        return HttpResponse('404')
    content = {'link': link}
    return render(request, 'redirect.html', content)


def create_link(request):
    link = request.POST['link']
    val = URLValidator(['http', 'https'])
    try:
        here = val(link)
    except ValidationError:
        return HttpResponse('Bad link, try again')
    new_link = Link(link=request.POST['link'], prefix=str(randint(0, 999999)))
    new_link.save()
    link = request.build_absolute_uri(location='/' + new_link.prefix)
    content = {'new_link': link}
    return render(request, 'created_link.html', content)
