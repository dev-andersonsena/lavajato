from django import forms
from .models import UserProfile
from .models import TIPOS_LAVAGEM_CHOICES, DIA_SEMANA_CHOICES, HORARIO_SEMANA_CHOICES


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





