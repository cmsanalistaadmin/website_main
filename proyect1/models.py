from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Aquí se encripta
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

CARGOS = (
    ('vendedor', 'Vendedor'),
    ('supervisor', 'Supervisor'),
    ('jefe', 'Jefe'),
)

SUPERVISORES = (
    ('Victor Murillo', 'Victor Murillo'),
    ('Marcos Nuñez', 'Marcos Nuñez'),
    ('Percy Apaza', 'Percy Apaza'),
    ('Gonzalo Alvarado', 'Gonzalo Alvarado'),
)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=20, choices=CARGOS)
    codigo_vendedor = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100, choices=SUPERVISORES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email
