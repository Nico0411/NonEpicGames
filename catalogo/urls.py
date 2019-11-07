from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[

	path('',views.index,name='index'),
	path('games/', views.GameListView.as_view(), name='game'),
	path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
	path('Login/',LoginView.as_view(),name="login_url"),
	path('register/', views.registerView.as_view(), name='register_url'),
	path('galery/', views.galery, name="galery_url")

]