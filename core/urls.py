from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),


    path('6eme/', views.sixieme, name='sixieme'),
    path('7eme/', views.septieme, name='septieme'),
    path('8eme/', views.huitieme, name='huitieme'),
    path('9eme/', views.neuvieme, name='neuvieme'),

    path('2nd/', views.seconde, name='seconde'),

   path('1ere_GFM/', views.premiere_gfm, name='premiere_gfm'),
  path('term_GFM/', views.terminal_gfm, name='terminal_gfm'),


path('1ere_OGHR/', views.premiere_ogrh, name='premiere_ogrh'),
  path('term_OGHR/', views.terminal_ogrh, name='terminal_ogrh'),

path('1ere_IAG/', views.premiere_iag, name='premiere_iag'),
  path('term_IAG/', views.terminal_iag, name='terminal_iag'),

path('TICE/', views.tice, name='tice'),
]