from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class registerForm(UserCreationForm):
	name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','id': 'inputName','placeholder':'Ingrese su nombre' }))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail','placeholder':'Ingrese su email'}))
	password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder':'Ingrese una Contraseña'}))
	password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputConfirmPassword', 'placeholder':'Confirme su Contraseña'}))

	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'name',
			'password1',
			'password2',
		)
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control','id':'inputUserName', 'placeholder':'Ingrese su nombre se usuario'}),
		}

		