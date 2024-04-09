from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, User

# Define um novo admin para User que estende o admin padrão do Django
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
