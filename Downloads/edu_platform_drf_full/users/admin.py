from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['email']
    list_display = ['email', 'phone', 'city', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('phone', 'city', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone', 'city', 'avatar', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
