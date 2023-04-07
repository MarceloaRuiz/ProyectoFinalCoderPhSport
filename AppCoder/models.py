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



class ComentarioMedicina(models.Model):
    comentario = models.ForeignKey(Plan_Medicina_Deportiva, related_name='comentariosMedicina', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)


class ComentarioKinesiologia(models.Model):
    comentario = models.ForeignKey(Plan_Kinesiologia_Fisioterapia, related_name='comentariosKinesiologia', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)


class ComentarioNutricion(models.Model):
    comentario = models.ForeignKey(Plan_Nutricion, related_name='comentariosNutricion', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)


class ComentarioPreparacionFisica(models.Model):
    comentario = models.ForeignKey(Plan_Preparacion_Fisica, related_name='comentariosPreparacionFisca', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)


class ComentarioPsicologia(models.Model):
    comentario = models.ForeignKey(Plan_Psicologia_Deportiva, related_name='comentariosPsicologia', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
