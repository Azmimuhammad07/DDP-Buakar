"""
URL configuration for projek_ddp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from berita.views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('page2/', page2, name='page2'),
    path('about/', about, name='about'),
    path('berita/berita1/', berita1, name='berita1'),
    path('berita/raffiahmad/', raffiahmad, name='raffiahmad'),
    path('berita/pagarlaut/', pagarlaut, name='pagarlaut'),
    path('berita/makansiang/', makansiang, name='makansiang'),
    path('berita/makansiang2/', makansiang2, name='makansiang2'),
    path('berita/ppn/', ppn, name='ppn'),
    path('berita/pagarlauttangerang/', pagarlauttangerang, name='pagarlauttangerang'),
    path('berita/sayur/', sayur, name='sayur'),
    path('berita/informatika/', informatika, name='informatika'),
    path('berita/koinjagat/', koinjagat, name='koinjagat'),
    path('exchange_rate/', exchange_rate, name='exchange_rate'), 
    path('calorie/', calorie_calculator, name='calorie_calculator'),
    path('muscle/', muscle_calculator, name='muscle_calculator'),
    path('olahraga', olahraga, name='olahraga'),
    path('arsenal-krisis-striker', arsenal_krisis_stiker, name='arsenal_krisis_striker'),
    path('prediksi_squad_timnas', prediksi_squad_timnas, name='prediksi_squad_timnas'),
    path('maguire', maguire, name='maguire'),
    path('pep_guardiola', pep_guardiola, name='pep_guardiola'),
    path('nottingham', nottingham, name='nottingham'),
    path('bulutangkis', bulutangkis, name='bulutangkis'),
    path('kurs/', exchange_rate, name='exchange_rate'),
    path('berita/raffiahmad/', raffiahmad, name='raffiahmad'),

    
]