from __future__ import unicode_literals

from django.db import models

#from app.departamento.models import Departamento

# Create your models here.
	
class Municipio(models.Model):
	codigo = models.PositiveIntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
    #departamento= models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	
