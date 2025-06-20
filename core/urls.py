from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('o-nas', views.about, name="about"),
    path('realizacie', views.realizations, name="realizations"),
    path('kontakt', views.contact, name="contact"),
    path('upload', views.upload, name="upload"),
]