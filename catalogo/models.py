from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Platform(models.Model):
    #Model representing a platform.

	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

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
  
class GameInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular game across whole library')
	game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
	publisher = models.CharField(max_length=200)
	reservation = models.DateField(null=True, blank=True)

	GAME_STATUS = (
		('a', 'Announced'),
		('o', 'Out of stock'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=GAME_STATUS,
		blank=True,
		default='a',
		help_text='Game availability',
	)

	class Meta:
		ordering = ['reservation']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.game.title})'

  
class Developer(models.Model):
	"""Model representing a developer."""
	name = models.CharField(max_length=100)


	def get_absolute_url(self):
		return reverse('developer-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name
