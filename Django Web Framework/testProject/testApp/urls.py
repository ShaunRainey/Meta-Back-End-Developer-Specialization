from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/', views.index),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('form/', views.showform),
    path("getform/", views.getform, name='getform'),
    path("template/<name>/", views.testTemplate, name='testTemplate'),
]