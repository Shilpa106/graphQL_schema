from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Category, Book, Grocery

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)

