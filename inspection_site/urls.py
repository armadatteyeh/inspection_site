from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.accueil, name='accueil'),



    path('sixieme/', views.sixieme, name='sixieme'),
    path('septieme/', views.septieme, name='septieme'),
    path('huitieme/', views.huitieme, name='huitieme'),
    path('neuvieme/', views.neuvieme, name='neuvieme'),

    path('seconde/', views.seconde, name='seconde'),

    path('premiere-gfm/', views.premiere_gfm, name='premiere_gfm'),
    path('terminal-gfm/', views.terminal_gfm, name='terminal_gfm'),

    path('premiere-ogrh/', views.premiere_ogrh, name='premiere_ogrh'),
    path('terminal-ogrh/', views.terminal_ogrh, name='terminal_ogrh'),

    path('premiere-iag/', views.premiere_iag, name='premiere_iag'),
    path('terminal-iag/', views.terminal_iag, name='terminal_iag'),

    path('tice/', views.tice, name='tice'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)