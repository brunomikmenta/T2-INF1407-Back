from django.urls import path
from MySongProfileAppBack import views

app_name = 'MySongProfileAppBack'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_page, name='login'),
	path('cadastroUsuario/', views.cadastroUsuario, name='cadastroUsuario'),
    path('esqueceuSenha/', views.esqueceuSenha, name='esqueceuSenha'),
	path('esqueceuSenha/reset/', views.esqueceuSenhaReset, name='esqueceuSenhaReset'),
	path('perfil/', views.perfil, name='perfil'),
	path('api/users/', views.CadastrarUsuarioView.as_view(), name='api_users'),
	path('api/login/', views.LoginUsuarioView.as_view(), name='api_login'),
	path('api/logout/', views.LogoutUsuarioView.as_view(), name='api_logout'),
	path('api/password-reset/', views.PasswordResetView.as_view(), name='api_password_reset'),
	path('api/profile/', views.ProfileView.as_view(), name='api_profile'),
    path('api/playlist/', views.PlaylistView.as_view(), name='api_playlist'),
    path('api/playlist/<int:song_id>/', views.PlaylistSongDetailView.as_view(), name='api_playlist_song_detail'),
    
]