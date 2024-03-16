from django.db import models
from datetime import date
import datetime
from django.db.models.base import Model

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    #categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    #usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nomeclass
    