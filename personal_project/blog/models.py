from django.db import models
import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    chamada = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='portfolio/images')
    conteudo = models.TextField()
    date = models.DateField(default=datetime.date.today)

