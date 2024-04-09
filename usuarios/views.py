from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import User, UserProfile
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm





def login_view(request):  # Renomeie sua view para login_view
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome_login')
            senha = form.cleaned_data.get('senha')
            usuario = authenticate(username=nome, password=senha)
            if usuario is not None:
                login(request, usuario)  # Use o login em vez de auth_login
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('carro')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome_cadastro')
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha_1')
            telefone = form.cleaned_data.get('telefone')
            if senha != form.cleaned_data.get('senha_2'):
                form.add_error('senha_2', 'As senhas não coincidem')
                return render(request, "usuarios/cadastro.html", {"form": form})
            if User.objects.filter(username=nome).exists():
                form.add_error('nome_cadastro', 'Este nome de usuário já está em uso')
                return render(request, "usuarios/cadastro.html", {"form": form})
            # Cria o usuário
            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            # Cria o UserProfile associado ao usuário
            UserProfile.objects.create(user=usuario)
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido

    return render(request, "usuarios/cadastro.html", {"form": form})

def escolher_modelo(request, modelo):
    # Verifique se o usuário está autenticado
    if request.user.is_authenticated:
        # Obtenha o perfil do usuário atual
        perfil_usuario = UserProfile.objects.get(user=request.user)
        # Atualize o modelo de carro preferido do usuário
        perfil_usuario.modelo_carro_preferido = modelo
        perfil_usuario.save()   
    
    # Redirecione o usuário para onde você deseja após a escolha do modelo
    return redirect('index')



def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('login')
    

def index_view(request):
    return render(request, 'index.html')

def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('login')
    

def index_view(request):
    return render(request, 'index.html')

def carro(request):
    return render(request, 'carro.html')

def tipoLavagem(request):
    return render(request, 'tipoLavagem/tipolavagem.html')

from django.shortcuts import get_object_or_404
from .models import User, UserProfile

def excluir_usuario(request, user_id):
    # Obtenha o usuário que será excluído
    user = get_object_or_404(User, pk=user_id)

    # Verifique se existe um UserProfile relacionado ao usuário
    if hasattr(user, 'userprofile'):
        # Obtenha o UserProfile relacionado
        user_profile = user.userprofile

        # Exclua o UserProfile
        user_profile.delete()

    # Agora você pode excluir o usuário
    user.delete()

    # Redirecione para onde você quiser após a exclusão
    return redirect('index')

def calendario(request):
    return render(request, 'calendario/calendario.html')
