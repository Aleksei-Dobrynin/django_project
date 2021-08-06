"""driverinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from accounts.views import logout, register, login
from django.contrib import admin
from django.urls import path
from news.views import news
from home_index.views import index
from travel.views import travel, travel_detail, travel_filter, travel_new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news, name='news'),
    path('', index , name='index'),
    path('travel/', travel, name='travel'),
    path('travel/<int:pk>/', travel_detail, name='travel_detail'),
    path('travel_filter/<int:pk>/', travel_detail, name='travel_detail'),
    path('travel_new/', travel_new, name='travel_new'),
    path('travel_filter/',travel_filter, name='travel_filter'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
