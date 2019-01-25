from django.db import models

# Create your models here.

class Post(models.Model):
    switch_ip = models.CharField("IP адресс оборудования", max_length=250)
    text = models.TextField("Список изменений")
    date_now = models.DateTimeField("Дата изменения", auto_now=True)

    def __str__(self):
        return self.switch_ip
