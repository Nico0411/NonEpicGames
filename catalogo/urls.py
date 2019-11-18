from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[

	path('',views.index,name='index'),
	path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
	path('Login/',LoginView.as_view(),name="login_url"),	
	path('galery/', views.galery, name="galery_url")

]

urlpatterns += [
    path('register/', views.registerView.as_view(), name='register_url'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='delete'),
]