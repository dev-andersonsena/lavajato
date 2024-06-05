from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, User, Funcionario, Agendamento, Dupla
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path  # Adicione esta importação
from usuarios.forms import FuncionarioForm, DuplaForm       
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
    list_display = ('dupla', 'nome', 'Parceiro')
    list_filter = ('dupla', 'nome')
    change_list_template = "admin/funcionario_changelist.html"  # Custom template for the change list view
    actions = ['delete_selected_funcionarios', 'delete_selected_duplas']  # Add actions


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
                return redirect('admin:usuarios_funcionario_changelist')  # Use o nome correto
        else:
            form = FuncionarioForm()
        return render(request, 'admin/add_funcionario.html', {'form': form})

    def add_dupla_view(self, request):
        if request.method == "POST":
            form = DuplaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:usuarios_funcionario_changelist')  # Use o nome correto
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
            if funcionario.dupla:
                funcionario.dupla = ""
                funcionario.save()
        self.message_user(request, "Duplas selecionadas foram apagadas com sucesso.")
    delete_selected_duplas.short_description = "Apagar Duplas"

admin.site.register(Funcionario, FuncionarioAdmin)

########### fim classe funcionaro #####################3



@admin.register(UserProfile)
class RelatoriosDeAgendamentosAdmin(admin.ModelAdmin):
        
    list_display = ('user', 'veiculo', 'modelo_carro_preferido', 'telefone', 'filial_preferida', 'tipo_lavagem', 'lavagem_adicional', 'horario', 'data_atual')
    
    def user_report_link(self, obj):
        url = reverse('admin:user_report', args=[obj.pk])
        return format_html('<a href="{}">Visualizar Relatório</a>', url)
    user_report_link.short_description = 'Relatório de Agendamentos'
    user_report_link.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:user_id>/report/', self.admin_site.admin_view(self.user_report_view), name='user_report'),
        ]
        return custom_urls + urls

    def user_report_view(self, request, user_id):
        # Implemente a visualização do relatório aqui
        pass

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets += (
            ('Relatório', {
                'fields': ('user_report_link',),
            }),
        )
        return fieldsets


############################## agendamento para os funcionarios das duplas #########################


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'funcionario', 'data_agendamento', 'horario', 'tipo_lavagem', 'lavagem_adicional', 'get_dupla_registrada')
    list_filter = ('data_agendamento', 'horario', 'tipo_lavagem', 'dupla_registrada')
    search_fields = ('user_profile__user__username', 'funcionario__nome', 'data_agendamento')
    fields = ('user_profile', 'funcionario', 'data_agendamento', 'horario', 'tipo_lavagem', 'lavagem_adicional', 'dupla_registrada')
    readonly_fields = ('data_agendamento',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            if 'data_agendamento' in form.base_fields:
                form.base_fields['data_agendamento'].initial = timezone.now().date()
        return form

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            if not obj.data_agendamento:
                obj.data_agendamento = timezone.now().date()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Se uma data de filtro foi enviada, filtra os agendamentos por essa data
        data_selecionada = request.GET.get('data_agendamento__gte')  # Data selecionada no filtro de data
        if data_selecionada:
            queryset = queryset.filter(data_agendamento=data_selecionada)
        return queryset

    def get_dupla_registrada(self, obj):
        return ''.join([str(dupla) for dupla in obj.dupla_registrada.all()])
    get_dupla_registrada.short_description = 'Dupla'

admin.site.register(Agendamento, AgendamentoAdmin)