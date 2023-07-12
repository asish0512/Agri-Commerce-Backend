"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import loads.views as loadviews
import sell.views as sellviews
import logistics.views as logviews
import buy.views as buyviews
import images.views as imageviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load/', loadviews.getAllLoads, name='getAllLoads'),
    path('load/createLoad/', loadviews.createLoad, name='createLoad'),
    path('load/mergeLoads/', loadviews.mergeLoads, name='mergeLoads'),
    path('load/<int:id>/', loadviews.getGoats, name='getGoats'),
    path('load/<int:id>/addGoat/', loadviews.addGoatToLoad, name='addGoat'),
    path('load/<int:id>/splitGoats/', loadviews.splitLoad, name='splitGoats'),
    path('sell/addSeller/', sellviews.addSeller, name='addSeller'),
    path('sell/getSells/', sellviews.getSells, name='getSells'),
    path('logistics/addConsign/', logviews.addConsign, name='addConsign'),
    path('logistics/getConsigns/', logviews.getConsigns, name='getConsigns'),
    path('buy/buyGoats', buyviews.buyGoats, name='buyGoats'),
    path('buy/getGoatsDest/<str:place>/', buyviews.getGoatsDest, name='getGoatsDest'),
    path('image/addAnnot/', imageviews.addAnnot, name='addAnnot'),
    path('image/getAnnots/<int:goatId>/', imageviews.getAnnots, name='getAnnots'),
]
