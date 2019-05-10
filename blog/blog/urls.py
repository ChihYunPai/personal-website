"""blog URL Configuration

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
from django.urls import path, include

from mainsite.views import homepage
from mainsite.views import showpost
from mainsite.views import about
from mainsite.views import productlist
from mainsite.views import displaydetail
from mainsite.views import tv
from mainsite.views import secondhandphone

productlist_pattern = [
    path('', productlist),
    path('<str:sku>/', displaydetail),
]

tv_pattern = [
    path('', tv, name='tv-url'),
    path('<int:tvno>/', tv, name='tv-url'),
]

secondhandphone_pattern = [
    path('', secondhandphone, name='secondhandphone-url'),
    path('<int:phoneno>/', secondhandphone, name='secondhandphone-url'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),
    path('about/', about),
    path('productlist/', include(productlist_pattern)),
    path('tv/', include(tv_pattern)),
    path('secondhandphone/', include(secondhandphone_pattern)),
]