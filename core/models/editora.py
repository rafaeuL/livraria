from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, null=True)
    site = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome