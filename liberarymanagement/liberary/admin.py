from django.contrib import admin
from .models import Book,StudentExtra,IssuedBook
# Register your models here.

admin.site.register(Book)
admin.site.register(StudentExtra)
admin.site.register(IssuedBook)
