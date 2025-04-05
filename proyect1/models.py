from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Crea un UserManager personalizado si deseas un control más detallado sobre la creación de usuarios
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, cargo, supervisor, codigo_ven, password):
        if not email:
            raise ValueError('El correo debe ser obligatorio')
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            name=name,
            cargo=cargo,
            supervisor=supervisor,
            codigo_ven=codigo_ven
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, cargo, supervisor, codigo_ven, password):
        user = self.create_user(
            email,
            name=name,
            cargo=cargo,
            supervisor=supervisor,
            codigo_ven=codigo_ven,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(models.Model):
    # Campos de la base de datos
    CORREO = models.EmailField(unique=True)
    CONTRASEÑA = models.CharField(max_length=128)
    CARGO_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('supervisor', 'Supervisor'),
        ('jefe', 'Jefe')
    ]
    CARGO = models.CharField(max_length=10, choices=CARGO_CHOICES)
    
    SUPERVISOR_CHOICES = [
        ('Victor Murillo', 'Victor Murillo'),
        ('Marcos Nuñez', 'Marcos Nuñez'),
        ('Percy Apaza', 'Percy Apaza'),
        ('Gonzalo Alvarado', 'Gonzalo Alvarado')
    ]
    SUPERVISOR = models.CharField(max_length=50, choices=SUPERVISOR_CHOICES)

    CODIGO_VEN = models.CharField(max_length=10, unique=True)
    NOMBRE = models.CharField(max_length=255)

    # Utiliza el CustomUserManager para manejar la creación de usuarios
    objects = CustomUserManager()

    def __str__(self):
        return self.NOMBRE

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
