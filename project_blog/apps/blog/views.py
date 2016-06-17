# coding: utf-8

from django.http import HttpResponse

def movie_list(request):
    IMDB = request.GET['IMDB']
    published = request.GET['published']
    year = request.GET['year']
    movie_name = request.GET['name']
    return HttpResponse("""
        <h1>Movie list goes here!!</h1>
        <p>Your search query is <strong>%s</strong></p>
        <p>Year is %s</p>
        <p>Published %s</p>
        <p>IMDB raiting %s</p>
    """ % (movie_name, year, published, IMDB))
