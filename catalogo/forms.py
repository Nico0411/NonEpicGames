from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class registerForm(UserCreationForm):
	name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'name',
			'password1',
			'password2',
		)

		