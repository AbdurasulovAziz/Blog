from django.contrib.auth.models import User
from django.db import models

from project import settings


# Create your models here.


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=255, default='Title')
    text = models.TextField('Текст', default='Text Field')
    data = models.DateTimeField('Дата создания', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статью'

    def __str__(self):
        return self.title
