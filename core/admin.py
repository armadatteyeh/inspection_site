from django.contrib import admin
from .models import Visite
class VisiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'total')

admin.site.register(Visite, VisiteAdmin)

admin.site.site_header = "Inspection DJIBOUTI"
admin.site.site_title = "Admin Inspection"
admin.site.index_title = "Tableau de bord"