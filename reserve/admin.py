from django.contrib import admin
from .models import Shelter,User,Reservation

admin.site.register(Shelter)
admin.site.register(User)
admin.site.register(Reservation)