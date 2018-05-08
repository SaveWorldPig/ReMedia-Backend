from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Database


def index(request):
    all_albums = Database.objects.all()
    html = ''
    for album in all_albums:
        url = '/Users/' + album.id + '/'
        html += '<a href="' + url + '"'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details for user id: " + str(album_id) + "</h2>")