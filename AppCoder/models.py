from django.db import models


class Plan_Medicina_Deportiva(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}"


class Plan_Nutricion(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}"


class Plan_Kinesiologia_Fisioterapia(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}"


class Plan_Preparacion_Fisica(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}"


class Plan_Psicologia_Deportiva(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}"



class Comentario(models.Model):
    comentario = models.ForeignKey(Plan_Medicina_Deportiva, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
