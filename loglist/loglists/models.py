from django.db import models
from django.http import HttpResponse

# Create your models here.

class Post(models.Model):
    switch_ip = models.CharField("IP адресс оборудования", max_length=250)
    text = models.TextField("Список изменений")
    date_now = models.DateTimeField("Дата изменения", auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    def __str__(self):
        return self.switch_ip + " " + str(self.text)


class Tag(models. Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.title