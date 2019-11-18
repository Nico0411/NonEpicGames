from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User

class registerForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'name',
			'password1',
			'password2',
		)

		widget = {
			'username': forms.TextInput(attrs={'class': 'form-control','id':'inputUserName', 'placeholder':'Ingrese su nombre se usuario'}),
			'name': forms.TextInput(attrs={'class': 'form-control','id': 'inputName','placeholder':'Ingrese su nombre' }),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail','placeholder':'Ingrese su email'}),			
			'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder':'Ingrese una Contraseña'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputConfirmPassword', 'placeholder':'Confirme su Contraseña'}),
		}