from django.db import models
import uuid


# Create your models here.
class Cliente(models.Model):
    uuid = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=120, verbose_name="Nome completo do cliente",
                            help_text="Informe o nome do cliente, evite o uso de caracteres especiais.", null=False)
    email = models.CharField(max_length=120, unique=True)
    cpf = models.CharField(max_length=11, null=True, editable=False, unique=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=40, blank=False)
