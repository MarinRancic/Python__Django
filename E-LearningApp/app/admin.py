from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik

# Register your models here.

#admin.site.register(Korisnik)

@admin.register(Korisnik)
class KorisnikAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Other', {'fields':('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Other', {'fields':('role', 'status')}),
    )