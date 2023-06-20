from django.db import models

# Create your models here.
class Colheitas(models.Model):
    id_colheita = models.AutoField(primary_key=True)
    cultura = models.TextField(max_length=40)
    data_plantio = models.DateField()
    data_colheita = models.DateField()
    quantidade_colhida = models.FloatField()