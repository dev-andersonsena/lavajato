from django import forms
from .models import UserProfile

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
       max_length=10,
       widget=forms.TextInput(
             attrs={
                
               "placeholder": "Digite seu telefone"
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