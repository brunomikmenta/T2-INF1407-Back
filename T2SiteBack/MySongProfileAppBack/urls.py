from django.urls import path
from MySongProfileAppBack import views

app_name = 'MySongProfileAppBack'

urlpatterns = [
    path('login/', views.login_page, name='login'),
	path('cadastroUsuario/', views.cadastroUsuario, name='cadastroUsuario'),
	path('api/users/', views.CadastrarUsuarioView.as_view(), name='api_users'),
	path('api/login/', views.LoginUsuarioView.as_view(), name='api_login'),
	path('api/logout/', views.LogoutUsuarioView.as_view(), name='api_logout'),
]