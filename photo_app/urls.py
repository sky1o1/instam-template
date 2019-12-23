"""instam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#importing index from photo app
from photo_app.views import index, add, edit, profile, delete, search
app_name = 'photo_app' 

urlpatterns = [
    
    #path('',index) #specifying path from view
    path('search/',search, name='search'),
    path('',index, name='index'),
    path('add',add,name='add'),
    path('profile/',profile,name='profile'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete'),
]
