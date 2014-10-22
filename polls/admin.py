from django.contrib import admin
from polls.models import Restaurant, Person, Dish, Choice
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Person)
admin.site.register(Dish)
admin.site.register(Choice)