from django.shortcuts import render
from .models import Game, Platform, GameInstance, Developer
from django.views import generic

# Create your views here.
def index(request):
	#Generar contadores de algunos objetos.
	games = Game.objects.all().order_by('title')

	#Renderiza la plantilla HTML index.html con los datos en las variables contexto
	context = {
		'games':games
	}
	return	render(request, 'index.html', context)

class GameListView(generic.ListView):
	model = Game
	paginate_by = 9
	
class GameDetailView(generic.DetailView):
	model = Game

		

	

