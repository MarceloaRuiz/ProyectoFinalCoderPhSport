
from django.db import models


class Plan_Medicina_Deportiva(models.Model):

    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero},  Descripcion: {self.descripcion}, Especialista: {self.especialista}, Paciente: {self.paciente}"


class Plan_Nutricion(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Descripcion: {self.descripcion}, Especialista: {self.especialista}, Paciente: {self.paciente}"


class Plan_Kinesiologia_Fisioterapia(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Descripcion: {self.descripcion}, Especialista: {self.especialista}, Paciente: {self.paciente}"


class Plan_Preparacion_Fisica(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Descripcion: {self.descripcion}, Especialista: {self.especialista}, Paciente: {self.paciente}"


class Plan_Psicologia_Deportiva(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    descripcion = models.TextField()
    especialista = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Descripcion: {self.descripcion}, Especialista: {self.especialista}, Paciente: {self.paciente}"