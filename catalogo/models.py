from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Platform(models.Model):
    #Model representing a platform.

	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class User(AbstractBaseUser):
	username = models.CharField(max_length=30)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password1 = models.CharField(max_length=30)
	password2 = models.CharField(max_length=30)

	USERNAME_FIELD = 'username'
	
	def __str__(self):
		return self.username



		
class Game(models.Model):
    
	title = models.CharField(max_length=200)
	developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True)
	launch = models.DateField(null=True, blank=True)   
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
	price = models.IntegerField('Price', default=0 ,help_text='Enter the price of the game in clp$')
	platform = models.ManyToManyField(Platform)
	image = models.ImageField()
	requirements = models.TextField(max_length=1000, help_text='Enter the systems requirements', default='No Requirements found')

	

    
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this game."""
		return reverse('game-detail', args=[str(self.id)])

		
class Developer(models.Model):
	"""Model representing a developer."""
	name = models.CharField(max_length=100)

	def __str__(self):
		"""String for representing the Model object."""
		return self.name



