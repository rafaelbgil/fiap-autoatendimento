from django.db import models
import uuid


# Create your models here.
class Cliente(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
