from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class AreaEstudo(models.Model):
    area = [
        ('CC', 'Ciência da Computação'),
        ('AS', 'Análise de Sistemas'),
        ('EG', 'Engenharias'),
        ('OU', 'Outros')
    ]
    curso_realizado = models.CharField(max_length=10 , choices=area)

    def __str__(self):
        return self.curso_realizado



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(BaseUserManager):
    ra = models.CharField(max_length=8)
    username = models.CharField(max_length=60)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Curso(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField()
    topicos = models.TextField()
    carga_horaria = models.IntegerField()
    image = models.ImageField(
        upload_to='courso/imagens', verbose_name='Imagem'
    )

    def __str__(self):
        return self.nome

class Turma(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    inscricao_inicio = models.DateField()
    inscricao_fim = models.DateField()
    arquivado = models.BooleanField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        nome = self.curso.__str__() + " " + self.data_inicio.__str__()
        return nome


