from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as aut_a
from django.contrib.auth import admin as auth_admin
# from django.contrib.auth import admin as auth_admin

from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserAdmin(auth_admin.UserAdmin):
    # The forms to add and change user instances
    readonly_fields=('time_created', 'time_updated')
   
    date_hierarchy = 'time_created'

    list_display = ('username', 'first_name', 'last_name', 'email', 'time_created', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('time_created',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser', 
            'groups'
            )
        }),
        ('Subscription', {
            'fields': ('active_subscription', 'subscription_start_date', 'subscription_end_date'),
        }),
        ('Time Information', {
            'fields': ('time_created', 'time_updated'),
        }),
    )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
