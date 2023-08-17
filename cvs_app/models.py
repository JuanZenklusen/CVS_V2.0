from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(null=True, blank=True)
    prefijo_cuil = models.IntegerField(null=True, blank=True)
    sufijo_cuil = models.IntegerField(null=True, blank=True)
    cod_area = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.CharField(max_length=60, null=True, blank=True)
    provincia = models.CharField(max_length=60, null=True, blank=True)
    nacionalidad = models.CharField(max_length=60, null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)
    day = models.IntegerField(null=True, blank=True,)
    month = models.IntegerField(null=True, blank=True,)
    year = models.IntegerField(null=True, blank=True,)
    foto = models.ImageField(default='default.jpg', upload_to='profile_images')
    estado_civil = models.CharField(max_length=40, null=True, blank=True)
    imprime_estado_civil = models.BooleanField(default=True)
    cantidad_hijos = models.CharField(max_length=10, null=True, blank=True, default="0")
    imprime_cantidad_hijos = models.BooleanField(default=True)
    editar_cv = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
    

class Academic_Level(models.Model):
    level = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.level
    
class Status(models.Model):
    status = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.status

class Academic_Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Academic_Level, on_delete=models.CASCADE)
    estado = models.ForeignKey(Status, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=80, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.escuela} - {self.nivel} - {self.estado}'