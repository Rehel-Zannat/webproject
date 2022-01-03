from django.urls import path
from projectApp import views
urlpatterns = [
    path('', views.help,name='help'),
]
