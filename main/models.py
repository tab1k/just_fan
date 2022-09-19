from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_upload = models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')
    is_published = models.BooleanField(default=True, verbose_name='Сохранить')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.time_upload >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    women_c = models.ForeignKey(Women, on_delete=models.CASCADE, verbose_name= 'Пост')
    author_name = models.CharField(max_length=25, verbose_name='Имя пользователя')
    comment_text = models.TextField(blank=True, verbose_name='Текст комментария')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

