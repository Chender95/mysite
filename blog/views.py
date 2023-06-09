from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1><i>страница не нашлась!</i></h1>')

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def shava(request):
    return render(request, 'blog/shava.html', {})

def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')