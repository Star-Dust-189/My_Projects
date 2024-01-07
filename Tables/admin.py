from django.contrib import admin

from .models import Food_Suplier,Food_Categories,Photographers,Photographer_works , Mackup_Artist,Mehndi_Artist,Venue_Provider,Venue_Type


admin.site.register(Food_Categories)
admin.site.register(Food_Suplier)

admin.site.register(Mackup_Artist)

admin.site.register(Mehndi_Artist)

admin.site.register(Photographers)
admin.site.register(Photographer_works)

admin.site.register(Venue_Type)
admin.site.register(Venue_Provider)
