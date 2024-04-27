from django.shortcuts import render, redirect
from .forms import DiaSemanaForm, LoginForms, CadastroForms, TipoLavagemForm, HorarioSemanaForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import User, UserProfile
from django.contrib.auth import authenticate, login
from .forms import CadastroForms, UserProfileForm
from django.contrib.auth.decorators import login_required
from .forms import FilialForm
from django.db.models import Count
from django.shortcuts import get_object_or_404



def index_view(request):
    return render(request, 'index.html')

def carro(request):
    return render(request, 'carro.html')

def calendario(request):
    return render(request, 'calendario/calendario.html')





login_required
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
                return redirect('home')
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
            telefone = form.cleaned_data.get('telefone')  # Acessando o telefone do formulário
            veiculo = form.cleaned_data.get('veiculo')
            
            print("Veículo:", veiculo) 

            if senha != form.cleaned_data.get('senha_2'):
                print("As senhas não coincidem:", senha, form.cleaned_data.get('senha_2'))
                form.add_error('senha_2', 'As senhas não coincidem')
                return render(request, "usuarios/cadastro.html", {"form": form})

            if User.objects.filter(username=nome).exists():
                print("Nome de usuário já em uso:", nome)
                form.add_error('nome_cadastro', 'Este nome de usuário já está em uso')
                return render(request, "usuarios/cadastro.html", {"form": form})

            # Cria o usuário
            print("Criando usuário...")
            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            print("Usuário criado:", usuario)
            
            # Cria o UserProfile associado ao usuário
            print("Criando UserProfile...")
            perfil = UserProfile.objects.create(user=usuario, telefone=telefone, veiculo=veiculo)
            print("UserProfile criado:", perfil)
            
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido

    return render(request, "usuarios/cadastro.html", {"form": form})





def escolher_modelo(request, modelo):
    if request.user.is_authenticated:
        perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
        perfil_usuario.modelo_carro_preferido = modelo
        perfil_usuario.save()
        
        if perfil_usuario.modelo_carro_preferido == 'HATCH':
            return redirect('tipolavagemHATCH')
        elif perfil_usuario.modelo_carro_preferido == 'SEDAN':
            return redirect('tipolavagemSEDAN')
        elif perfil_usuario.modelo_carro_preferido == 'SUV':
            return redirect('tipolavagemSUV')
        elif perfil_usuario.modelo_carro_preferido == 'PICAPE':
            return redirect('tipolavagemPICAPE')
        elif perfil_usuario.modelo_carro_preferido == 'MOTO':
            return redirect('tipolavagemMOTO')
        elif perfil_usuario.modelo_carro_preferido == 'MOTO2':
            return redirect('tipolavagemMOTO#2')

    return redirect('index')


def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('login')
    



#def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('index')
    

@login_required
def home(request):
    form = FilialForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            filial = form.cleaned_data.get('filial_primavera') or form.cleaned_data.get('filial_horto')
            messages.info(request, f'Filial selecionada: {filial}')
            print("Filial selecionada:", filial)  # Imprime no terminal do servidor


            perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
            perfil_usuario.filial_preferida = filial
            perfil_usuario.save()

            return redirect('carro')

    return render(request, 'home.html', {'form': form})


def tipoLavagem(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemHATCH.html', {'form': form})

def tipoLavagem2(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemSEDAN.html', {'form': form})

def tipoLavagem3(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemPICAPE.html', {'form': form})

def tipoLavagem4(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemSUV.html', {'form': form})

def tipoLavagem5(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemMOTO.html', {'form': form})

def tipoLavagem6(request):
    if request.method == 'POST':
        form = TipoLavagemForm(request.POST)
        if form.is_valid():
            tipo_lavagem_selecionado = form.cleaned_data['tipo_lavagem']
            perfil_usuario = request.user.userprofile
            perfil_usuario.tipo_lavagem = tipo_lavagem_selecionado
            perfil_usuario.save()
            print(f"Lavagem selecionada: {tipo_lavagem_selecionado}")  # Mensagem de depuração
            return redirect('calendario')  # Redireciona para a página 'calendario' após salvar
    else:
        form = TipoLavagemForm()
    return render(request, 'tipolavagem/tipolavagemMOTO#2.html', {'form': form})
  
def calendario(request):
    if request.method == 'POST':
        form = DiaSemanaForm(request.POST)
        if form.is_valid():
            dia_semana_selecionado = form.cleaned_data['dia_semana']
            perfil_usuario = request.user.userprofile
            perfil_usuario.dia_semana = dia_semana_selecionado
            perfil_usuario.save()
            print(f"dia selecionado: {dia_semana_selecionado}")  # Mensagem de depuração
            return redirect('horario')  # Redireciona para a página 'horario' após salvar
        else:
            print("Formulário inválido:", form.errors)  # Adicione esta linha para ver os erros de validação do formulário
    else:
        form = DiaSemanaForm()
    return render(request, 'calendario/calendario.html', {'form': form})

from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

def horario(request):
    if request.method == 'POST':
        form = HorarioSemanaForm(request.POST)
        if form.is_valid():
            hora_semana_selecionado = form.cleaned_data['horario_semana']
            
            # Verifica se o usuário já possui um UserProfile
            perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
            
            # Verifica se há mais de um agendamento para o horário selecionado
            if UserProfile.objects.filter(horario=hora_semana_selecionado).count() >= 2:
                messages.error(request, 'O limite de agendamentos para este horário foi atingido.')
                return redirect('pagina_de_agendamento')
            
            # Atualiza o horário do UserProfile do usuário
            perfil_usuario.horario = hora_semana_selecionado
            perfil_usuario.save()
            
            print(f"dia selecionado: {hora_semana_selecionado}")  # Mensagem de depuração
            return redirect('index')  # Redireciona para a página 'horario' após salvar
        else:
            print("Formulário inválido:", form.errors)  # Adicione esta linha para ver os erros de validação do formulário
    else:
        form = HorarioSemanaForm()
    return render(request, 'calendario/escolher_horario.html', {'form': form})
from django.shortcuts import get_object_or_404

def horario(request):
    if request.method == 'POST':
        form = HorarioSemanaForm(request.POST)
        if form.is_valid():
            hora_semana_selecionado = form.cleaned_data['horario_semana']
            
            # Verifica se o usuário já possui um UserProfile
            perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
            
            # Verifica se há mais de um agendamento para o horário selecionado
            if UserProfile.objects.filter(horario=hora_semana_selecionado).count() >= 2:
                messages.error(request, 'O limite de agendamentos para este horário foi atingido.')
                return redirect('escolher_horario')
            
            # Atualiza o horário do UserProfile do usuário
            perfil_usuario.horario = hora_semana_selecionado
            perfil_usuario.save()
            
            print(f"dia selecionado: {hora_semana_selecionado}")  # Mensagem de depuração
            return redirect('index')  # Redireciona para a página 'horario' após salvar
        else:
            print("Formulário inválido:", form.errors)  # Adicione esta linha para ver os erros de validação do formulário
    else:
        form = HorarioSemanaForm()
    return render(request, 'calendario/escolher_horario.html', {'form': form})





