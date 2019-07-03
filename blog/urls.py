from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home_page_url'),
    path('about/', about_page, name = 'about_page_url')
]
