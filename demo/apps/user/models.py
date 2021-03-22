from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    first_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="Nombre(s)"
    )
    last_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="Apellidos"
    )
    email = models.EmailField(null=True, blank=False, verbose_name="Correo electrónico")

    username_scorm = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="ID en SCORM"
    )

    id_user_scorm = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="ID en SCORM"
    )

    id_course_scorm = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="ID del curso en SCORM"
    )

    id_level_scorm = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="ID del nivel en SCORM"
    )

    avatar = models.CharField(
        max_length=300, null=True, blank=False, verbose_name="Avatar seleccionado"
    )


    score = models.CharField(
        max_length=1000, null=False, blank=False, verbose_name="Puntuación"
    )
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.pk)
