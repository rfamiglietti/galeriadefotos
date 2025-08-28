# fotos/models.py

from django.db import models
from datetime import datetime

# Create models.
class Fotografia(models.Model):
    nome = models.CharField(max_length=100)
    legenda = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100, default='')
    descricao = models.TextField()
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_foto = models.DateField(default=datetime.now)
    publicada = models.BooleanField(default=True)

    def __str__(self):
        return self.nome