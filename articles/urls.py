from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articleHome, name="articlehome"),
    path('arduino', views.codingHome, name="codinghome"),
    path('robotics', views.roboticsHome, name="roboticshome"),
    path('search/', views.search, name="search"),
    path('create/', views.create, name="create"),
    path('error', views.error, name="error"),
    path("tag/<slug:slug>/", views.Tagging, name='tagged'),
    path('<str:slug>', views.articlePost, name="articlePost"),
]
