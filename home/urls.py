from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('prof_setting', views.setting, name="setting"),
]
