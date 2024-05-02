from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, User, Funcionario, Agendamento
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path  # Adicione esta importação


# Define um novo admin para User que estende o admin padrão do Django
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'veículo')}),
    )

admin.site.register(User, UserAdmin)

admin.site.register(Funcionario)


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_agendamento', 'horario')  # Especifica os campos a serem exibidos na lista

admin.site.register(Agendamento, AgendamentoAdmin)



@admin.register(UserProfile)
class RelatoriosDeAgendamentosAdmin(admin.ModelAdmin):
        
    list_display = ('user', 'telefone', 'modelo_carro_preferido', 'filial_preferida', 'tipo_lavagem', 'horario', 'data_atual')
    
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
