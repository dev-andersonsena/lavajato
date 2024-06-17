from django import forms
from .models import UserProfile, Funcionario, Agendamento
from .models import TIPOS_LAVAGEM_CHOICES, DIA_SEMANA_CHOICES, HORARIO_SEMANA_CHOICES
from django.forms.widgets import SelectDateWidget
from django.conf import settings

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="nome",
        required=True,
        max_length=100
        
    )
   
    senha=forms.CharField(
        label="senha",
        required=True,
        max_length=10,
        widget=forms.PasswordInput(
              attrs={
                "placeholder": "Digite sua senha"
            }
        )
        # permite a edição de algumas caracteristicas do input
    )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex: João Silva"
            }
        )
    )
        
    email = forms.EmailField(
        label="email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
           attrs={
                "placeholder": "Ex: email@gmail.com"
            }
        )
    )
        
    senha_1 = forms.CharField(
        label="senha_1",
        required=True,
        max_length=10,
        widget=forms.PasswordInput(
             attrs={

                "placeholder": "Digite sua senha"
           }
        )
    )
    
    senha_2 = forms.CharField(
        label="senha_2",
        required=True,
        max_length=10,
        widget=forms.PasswordInput(
             attrs={
                 
                 "placeholder": "Digite sua senha novamente"
           }
       )
    )
        
    telefone = forms.CharField(
       label="telefone",
       required=True,
       max_length=11,
       widget=forms.TextInput(
             attrs={
                
               "placeholder": "Digite seu telefone"
           }
)
    )
    
    veiculo = forms.CharField(
       label="veiculo",
       required=True,
       max_length=50,
       widget=forms.TextInput(
             attrs={
                
                "placeholder": "Ex: Toyota"
           }
)
    )
    


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telefone', 'modelo_carro_preferido']
        

class FilialForm(forms.Form):
    filial_primavera = forms.CharField(widget=forms.HiddenInput(), initial='primavera')
    filial_horto = forms.CharField(widget=forms.HiddenInput(), initial='horto')
    
class TipoLavagemForm(forms.Form):
    tipo_lavagem = forms.ChoiceField(choices=TIPOS_LAVAGEM_CHOICES, widget=forms.RadioSelect)
    
class TipoLavagemAdicionalForm(forms.Form):
    lavagem_adicional = forms.ChoiceField(choices=TIPOS_LAVAGEM_CHOICES, widget=forms.RadioSelect)
    
class DiaSemanaForm(forms.Form):
    dia_semana = forms.ChoiceField(choices=DIA_SEMANA_CHOICES, widget=forms.RadioSelect)
    
class HorarioSemanaForm(forms.Form):
    horario_semana = forms.ChoiceField(choices=HORARIO_SEMANA_CHOICES, widget=forms.RadioSelect)

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome']  


class DuplaForm(forms.ModelForm):
    
    nome = forms.ModelChoiceField(
        queryset=Funcionario.objects.all(),
        label="nome",
        required=False,
        widget=forms.Select
    )
    Parceiro = forms.ModelChoiceField(
        queryset=Funcionario.objects.all(),
        required=False,
        label="Parceiro"
    )

    dupla = forms.CharField(
        label="Dupla",
        required=True,
        widget=forms.TextInput()
    )
    class Meta:
        model = Funcionario
        fields = ['nome', 'dupla', 'Parceiro']

    def __init__(self, *args, **kwargs):
        super(DuplaForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['dupla'].initial = self.instance.chave

    def save(self, commit=True):
        instance = super(DuplaForm, self).save(commit=False)
        instance.chave = self.cleaned_data['dupla']  # Salvando o nome da dupla inserido
        if commit:
            instance.save()
        return instance
    
    
    def __init__(self, *args, **kwargs):
        super(DuplaForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['nome'].initial = self.instance.chave

    
    

class AgendamentoForm(forms.ModelForm):
    Clientes = forms.ModelChoiceField(
        queryset=UserProfile.objects.all(),
        label="Clientes",
        widget=forms.Select
    )

    funcionario = forms.ModelChoiceField(
        queryset=Funcionario.objects.all(),
        label="Dupla",
        widget=forms.Select
    )

    data_agendamento = forms.DateField(
        label='Data do Agendamento',
        widget=forms.SelectDateWidget()
    )

    horario = forms.ChoiceField(
        label='Horário',
        choices=HORARIO_SEMANA_CHOICES,
        widget=forms.Select
    )

    class Meta:
        model = Agendamento
        fields = ['Clientes', 'funcionario', 'data_agendamento', 'horario']

    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].label_from_instance = lambda obj: obj.chave
        if self.instance and hasattr(self.instance, 'user_profile'):
            self.fields['Clientes'].initial = self.instance.user_profile

    def save(self, commit=True):
        instance = super(AgendamentoForm, self).save(commit=False)
        instance.user_profile = self.cleaned_data['Clientes']
        if commit:
            instance.save()
        return instance