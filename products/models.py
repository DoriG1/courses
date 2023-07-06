from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    city = models.CharField(max_length=255, verbose_name="Город")
    content = content = models.TextField(blank=True, verbose_name="Биография")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото")

    def __str__(self):
        return self.name



class Course(models.Model): 
    title = models.CharField(max_length=255, verbose_name="Наименование") #определяет тектовое поле с максимальной длинной
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") #отображение по слагу
    content = models.TextField(blank=True, verbose_name="Описание товара")   #расширенное текстовое поле
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото") #хранит ссылку на нашу фотографию поста, аплоуд говорит о том, в какой каталог будет идти наше фото
    price = models.IntegerField()
    time = models.IntegerField(verbose_name="Продолжительность")
    date_start = models.CharField(max_length=255, verbose_name="Старт курса")
    level = models.CharField(max_length=255, verbose_name="Уровень", null=True)
    teacher = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Преподаватель", null=True)

    def __str__(self):
        return self.title
    
    
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_slug': self.slug})
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    people = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total(self):
        total = self.course.price * self.people
        return total
    