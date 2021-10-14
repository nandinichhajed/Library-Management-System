from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.first_name + '['+str(self.enrollment)+']'

    @property
    def get_name(self):
        return self.user.first_name

    @property
    def getuserid(self):
        return self.user.id

class Book(models.Model):
    catchoices = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'comics'),
        ('biography', 'biography'),
        ('history', 'history'),
        ('novel', 'novel'),
        ('fantasy', 'fantasy'),
        ('thriller', 'thriller'),
        ('romance', 'romance'),
        ('scifi', 'Sci-Fi'), 
    ]
    name = models.CharField(max_length=50)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50,choices=catchoices,default='education')

    def get_expiry():
        return datetime.today() + timedelta(days = 10)

class IssuedBook(models.Model):
    enrollment = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default = get_expiry)

    def __str__(self):
        return self.enrollment

