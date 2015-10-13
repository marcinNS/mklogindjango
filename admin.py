from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from mklogin.models import MyUser,Kategoria

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'Użytkownicy'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MyUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Kategoria)