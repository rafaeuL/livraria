from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, Categoria, Editora, Livro, User, Compra, ItensCompra, Favoritos
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ["id"]
    list_display = ["email", "name"]
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    
    readonly_fields = ["last_login"]
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        try:
            # Chama o método original para salvar o usuário
            super().save_model(request, obj, form, change)
        except IntegrityError as e:
            raise

# Registre o User no Admin (não duplicar)
admin.site.register(User, UserAdmin)

# Registre as outras models
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    list_per_page = 10

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 10

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade')
    search_fields = ('nome', 'email', 'cidade')
    list_filter = ('nome', 'email', 'cidade')
    ordering = ('nome', 'email', 'cidade')
    list_per_page = 10

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1 # Quantidade de itens adicionais

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    search_fields = ("usuario", "status")
    list_filter = ("usuario", "status")
    ordering = ("usuario", "status")
    list_per_page = 25
    inlines = [ItensCompraInline]

@admin.register(Favoritos)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_adicionado')
    search_fields = ('usuario__email', 'livro__titulo')
