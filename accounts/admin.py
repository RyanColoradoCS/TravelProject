from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    #add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)
    # Override add_fieldsets to avoid issues with non-existent fields 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'age', 'is_staff')}
        ),
    )
    # https://forum.djangoproject.com/t/when-i-add-new-user-from-admin-panel-this-error-help/35124/8



admin.site.register(CustomUser, CustomUserAdmin)
