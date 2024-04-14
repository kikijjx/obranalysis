"""
URL configuration for obranalysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('load_template/', views.load_template, name='load_template'),
    path('update_graph1/', views.update_graph1, name='update_graph1'),
    path('update_graph2/', views.update_graph2, name='update_graph2'),
    path('update_graph3/', views.update_graph3, name='update_graph3'),
    path('update_graph4/', views.update_graph4, name='update_graph4'),
    path('update_graph5/', views.update_graph5, name='update_graph5'),
    path('update_graph6/', views.update_graph6, name='update_graph6'),
    path('generate_press_release/', views.generate_press_release, name='generate_press_release'),

]
