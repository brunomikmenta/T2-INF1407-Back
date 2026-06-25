from django.db import models


GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('N', 'Prefiro não dizer'),
]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    firstName = models.CharField('Nome', blank=True, max_length=30)
    lastName = models.CharField('Sobrenome', blank=True, max_length=30)
    gender = models.CharField('Gênero', blank=True, max_length=1, choices = GENDER_CHOICES)
    email = models.EmailField(max_length=254, unique=True)
    senha = models.CharField(max_length=15)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)