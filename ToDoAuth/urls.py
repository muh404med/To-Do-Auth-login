"""ToDoAuth URL Configuration

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
from django.contrib import admin
from django.urls import path
from major import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('currentpage/', views.current, name='current'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('create/', views.create, name='create'),
    path('completed/', views.completed, name='completed'),
    path('todo/<int:todoid_pk>', views.todoid, name='todoid'),
    path('todo/<int:todoid_pk>/complete>', views.complete, name='complete'),
    path('todo/<int:todoid_pk>/delete>', views.delete, name='delete'),


]

