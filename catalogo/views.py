from django.shortcuts import render, redirect
from .models import Game, Platform, Developer, User
from django.views import generic
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from .forms import registerForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	#Generar contadores de algunos objetos.
	num = request.session.get('num')
	if not num:
		num = 'price'
	request.session['num'] = num
	if request.method == 'POST':
		request.session['num'] = request.POST['orden']
	num = request.session.get('num')
	game_list = Game.objects.all().order_by(num)
	paginator = Paginator(game_list, 6)
	page = request.GET.get('page')
	games = paginator.get_page(page)
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	#Renderiza la plantilla HTML index.html con los datos en las variables contexto
	return	render(request, 'index.html', context={'games':games,'num_visits':num_visits},)


class GameDetailView(generic.DetailView):
	model = Game

class registerView(CreateView):
	model = User
	form_class = registerForm

	def form_valid(self, form):
		form.save()
		user = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username= user, password=password)
		login(self.request, user)
		return redirect('/catalogo/login/')
	


class ProfileUpdate(UpdateView):
	model = User
	field = ['username','name','email']
	
class ProfileDelete(DeleteView):
	model = User
	success_url = reverse_lazy('profile')		


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




		

	

