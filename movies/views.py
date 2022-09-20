from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies' : [
        {
            'id' : 777,
            'title' : 'Joji',
            'year' : 1969,
        },
        {
            'id' : 221,
            'title' : 'Alien',
            'year' : 1999,
        },
        {
            'id' : 55,
            'title' : 'Cheech and Chong',
            'year' : 2000,
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home")
