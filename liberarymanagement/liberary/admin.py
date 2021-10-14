from django.contrib import admin
from . models import StudentExtra,Book,IssuedBook

# Register your models here.
admin.site.register(StudentExtra)
admin.site.register(Book)
admin.site.register(IssuedBook)