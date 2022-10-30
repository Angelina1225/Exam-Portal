"""Onlineportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path, include
from student.views import stdloginpage, logoutUser, std_acc
from teacher.views import teacherloginpage, logoutUser, teacher_acc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_std/', std_acc, name = 'register1'),
    path('register_teacher/', teacher_acc, name = 'register2'),
    path('login_std/', stdloginpage, name = 'login1'),
    path('login_teacher/', teacherloginpage, name = 'login2'),
    path('logout/', logoutUser, name = 'logout1'),
    path('accounts/', include('django.contrib.auth.urls')),
]
