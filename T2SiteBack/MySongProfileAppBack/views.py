from django.shortcuts import render

from MySongProfileAppBack.serializers import UserSerializer
from rest_framework.views import APIView
from MySongProfileAppBack.models import User
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

@ensure_csrf_cookie
def cadastroUsuario(request):
    return render(request, 'cadastroUsuario.html')


class CadastrarUsuarioView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUsuarioView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '')

        if not username or not password:
            return Response({'detail': 'Username e password são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username, senha=password)
        except User.DoesNotExist:
            return Response({'detail': 'Usuário ou senha inválidos.'}, status=status.HTTP_401_UNAUTHORIZED)

        request.session['usuario_id'] = user.id
        request.session['usuario_username'] = user.username

        return Response({'success': True, 'username': user.username}, status=status.HTTP_200_OK)


class LogoutUsuarioView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        request.session.flush()
        return Response({'success': True}, status=status.HTTP_200_OK)
    
