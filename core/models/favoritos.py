from django.db import models
from django.conf import settings
from .livro import Livro

class Favoritos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favoritos")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="favoritos")
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "livro")

    def __str__(self):
        return f"{self.usuario.email} - {self.livro.titulo}"