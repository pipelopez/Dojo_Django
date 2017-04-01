from django.db import models

# Create your models here.
class Pelicula(models.Model):
	
	nombre = models.CharField(max_length=100, primary_key=True)
	sinopsis = models.CharField(max_length= 500)
	fecha_publicacion = models.DateField()
	categoria = models.CharField(max_length=30)


	def __str__(self):
		return self.nombre
