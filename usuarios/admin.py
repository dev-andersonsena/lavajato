from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, User, Funcionario, Agendamento
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path  # Adicione esta importação
from usuarios.forms import FuncionarioForm, DuplaForm, AgendamentoForm    
from django.shortcuts import render, redirect
from django.utils import timezone

# Define um novo admin para User que estende o admin padrão do Django
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'veículo')}),
    )

admin.site.register(User, UserAdmin)



############# funcionario duplas ############

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('get_dupla', 'nome', 'get_parceiro')
    list_filter = ('chave', 'nome', 'Parceiro')
    change_list_template = "admin/funcionario_changelist.html"
    actions = ['delete_selected_funcionarios', 'delete_selected_duplas']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add-funcionario/', self.admin_site.admin_view(self.add_funcionario_view), name='add-funcionario'),
            path('add-dupla/', self.admin_site.admin_view(self.add_dupla_view), name='add-dupla'),
        ]
        return custom_urls + urls

    def add_funcionario_view(self, request):
        if request.method == "POST":
            form = FuncionarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:usuarios_funcionario_changelist')
        else:
            form = FuncionarioForm()
        return render(request, 'admin/add_funcionario.html', {'form': form})

    def add_dupla_view(self, request):
        if request.method == "POST":
            form = DuplaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:usuarios_funcionario_changelist')
        else:
            form = DuplaForm()
        return render(request, 'admin/add_dupla.html', {'form': form})

    def delete_selected_funcionarios(self, request, queryset):
        for funcionario in queryset:
            funcionario.delete()
        self.message_user(request, "Funcionários selecionados foram apagados com sucesso.")
    delete_selected_funcionarios.short_description = "Apagar Funcionários"

    def delete_selected_duplas(self, request, queryset):
        for funcionario in queryset:
            if funcionario.Parceiro:
                funcionario.Parceiro = None
                funcionario.save()
        self.message_user(request, "Duplas selecionadas foram apagadas com sucesso.")
    delete_selected_duplas.short_description = "Apagar Duplas"

    def get_dupla(self, obj):
        return obj.chave
    get_dupla.short_description = 'Dupla'

    def get_parceiro(self, obj):
        return obj.Parceiro.nome if obj.Parceiro else ''
    get_parceiro.short_description = 'Parceiro'

admin.site.register(Funcionario, FuncionarioAdmin)
########### fim classe funcionaro #####################3



@admin.register(UserProfile)
class RelatoriosDeAgendamentosAdmin(admin.ModelAdmin):
    list_display = ('get_cliente', 'veiculo', 'modelo_carro_preferido', 'telefone', 'filial_preferida', 'tipo_lavagem', 'lavagem_adicional', 'horario', 'data_atual')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Remove o campo 'user_report_link' dos fieldsets
        return fieldsets   
    
    def get_cliente(self, obj):
        return obj.user
    get_cliente.short_description = 'Cliente'

############################## agendamento para os funcionarios das duplas #########################


class AgendamentoAdmin(admin.ModelAdmin):
    form = AgendamentoForm
    list_display = ('get_clientes', 'get_funcionario_chave', 'data_agendamento', 'horario')
    list_filter = ('data_agendamento', 'horario')
    search_fields = ('user_profile__user__username', 'funcionario__chave', 'data_agendamento')

    def get_clientes(self, obj):
        return obj.user_profile
    get_clientes.short_description = 'Clientes'

    def get_funcionario_chave(self, obj):
        return obj.funcionario.chave
    get_funcionario_chave.short_description = 'Chave do Funcionário'

admin.site.register(Agendamento, AgendamentoAdmin)

