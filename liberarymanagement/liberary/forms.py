from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':3, 'cols':30}))

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'password'] 

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'isbn', 'author', 'category']

class IssuedBook(forms.ModelForm):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.object.all(), empty_label="name and isbn", to_field_name="isbn", label="Name and Isbn")
    enrollment2 = forms.ModelChoiceField(queryset=models.StudentExtra.object.all(), empty_label="name and enrollment", to_field_name="enrollment", label="Name and Enrollment")


