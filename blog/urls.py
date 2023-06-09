from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('shava/', shava, name='shava'),
    re_path('r^archive/(?P<year>[0-9]{4})/', archive)
]