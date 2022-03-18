from django.db import models

# Create your models here.
from apps.home.models import TimeStampedModel


class Video(TimeStampedModel):
    link = models.URLField(max_length=1000)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Тип"

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статус"

    def __str__(self):
        return f"{self.name}"


class Blog(TimeStampedModel):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    subtitle = models.CharField(max_length=255)
    sub_description = models.TextField()
    status = models.ForeignKey('main.Status',
                               related_name='blogs',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    category = models.ForeignKey('main.Category',
                                 related_name='blogs',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    type = models.ForeignKey('main.Type',
                             related_name='blogs',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог>"

    def __str__(self):
        return f"{self.title}"


class Questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = "Вопросы-ответы"
        verbose_name_plural = "Вопросы-ответы"

    def __str__(self):
        return f"{self.question}"


class Covid(TimeStampedModel):
    city = models.CharField(max_length=255)
    get_sick_plus = models.IntegerField(default=0)
    get_sick_minus = models.IntegerField(default=0)
    recovered_plus = models.IntegerField(default=0)
    recovered_minus = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Ковид"
        verbose_name_plural = "Ковид"

    def __str__(self):
        return f"{self.city}"
