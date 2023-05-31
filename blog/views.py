from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1><i>страница не нашлась!</i></h1>')

def post_list(request):
    return HttpResponse('<h1>Главная страница. Пишу через HttpResponse. Крутая штука но на ней далеко не уйдешь!')


def shava(request):
    return render(request, 'blog/shava.html', {})