from django.shortcuts import render, redirect
from .models import Game, Platform, GameInstance, Developer, Profile
from django.views import generic
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .forms import registerForm

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

class registerView(CreateView):
	model = Profile
	form_class = registerForm

	def form_valid(self, form):
		form.save()
		user = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username= user, password=password)
		login(self.request, user)
		return redirect('/catalogo/Login/')


class LoginView(TemplateView):
	template_name = 'catalogo/Login.html'

def galery(request):
	
	games = Game.objects.all()

	#Renderiza la plantilla HTML index.html con los datos en las variables contexto
	context = {
		'games':games
	}
	return	render(request, 'catalogo/galery.html', context)
		
		

"""def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form = UserCreationForm()
		pass
	return render(request, 'registration/register.html',{'form':form } )
"""




		

	

