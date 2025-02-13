from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    ValidationError,
)

from core.models import Favoritos, Livro

class FavoritosSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    livro = CharField(source="livro.titulo", read_only=True)

    class Meta:
        model = Favoritos
        fields = ("id", "usuario", "livro", "data_adicionado")

class FavoritosCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Favoritos
        fields = ("usuario", "livro")

    def validate(self, data):
        usuario = data["usuario"]
        livro = data["livro"]

        if Favoritos.objects.filter(usuario=usuario, livro=livro).exists():
            raise ValidationError("Este livro já está nos favoritos.")
        
        return data