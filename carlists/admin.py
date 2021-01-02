from django.contrib import admin

from .models import Car_Listings

class CarListingAdmin(admin.ModelAdmin):

   list_display = ('title','rent_perday','is_Available','list_date')
   list_display_links = ('title','rent_perday')
#  list_filter = ('category',)
   list_editable = ('is_Available',)
   search_fields=('title','rent_perday','is_Available','list_date')
   list_per_page=25





admin.site.register(Car_Listings,CarListingAdmin)


