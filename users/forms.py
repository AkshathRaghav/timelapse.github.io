from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class send(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email   

# class UserRegister(UserCreationForm) :
#     STATES = (
#     ('', 'Choose...'),
#     ('MG', 'Minas Gerais'),
#     ('SP', 'Sao Paulo'),
#     ('RJ', 'Rio de Janeiro')
#     )
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput())
#     school = forms.CharField()
#     event = forms.ChoiceField(choices=STATES)
#     zip_code = forms.CharField(label='Zip')
#     check_me_out = forms.BooleanField(required=False)