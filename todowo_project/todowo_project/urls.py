"""todowo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #auth
    path('signup/', signupuser, name='signupuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('login/', loginuser, name='logintuser'),
    #Todos
    path('', home, name='home'),
    path('create/', createdtodo, name='createdtodo'),
    path('current/', currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>', todo, name='todo'),
    path('todo/<int:todo_pk>/complete', completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', deletetodo, name='deletetodo'),
    path('completed/', Completed, name='completed'),

]
