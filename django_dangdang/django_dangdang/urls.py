"""django_dangdang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include(('home_page_app.urls','home'))),
    path('user/',include(('user_app.urls','user'))),
    path('shopping/',include(('cart_app.urls','shopping'))),
    path('order/',include(('order_app.urls','order'))),
    path('commodity_management/',include(('commodity_management_app.urls','commodity_management'))),
]