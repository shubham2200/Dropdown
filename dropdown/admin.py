from django.contrib import admin

# Register your models here.
from . models import city, Country, Person,state

admin.site.register(city)
admin.site.register(Country)
admin.site.register(Person)
admin.site.register(state)