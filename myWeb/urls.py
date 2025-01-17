"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from shop.views import shop
from stock.views import stock
from message.views import message
from index.views import home
from food.views import food
from book.views import book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', shop),
    path('stock/', stock),
    path('message/', message),
    path('', home),
    path('food/', food),
    path('book/', book),
]
