from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
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
    
#     # class Meta:
#     #     verbose_name = 'Известные женщины'
#     #     verbose_name_plural = 'Известные женщины'
#     #     ordering = ['-time_create', 'title']



# # Модель Customer используется для хранения информации о клиентах, включая связь с объектом User из модели аутентификации Django (user), 
# # имя клиента (name) и адрес электронной почты (email). Модель также предоставляет метод для получения строкового представления клиента.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# # Модель Order используется для хранения информации о заказах пользователей, 
# # включая связь с покупателем (customer), дату заказа (date_order),
# # статус завершенности (complete), идентификатор транзакции (transaction_id) и методы для получения общей стоимости и количества товаров в заказе.
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     # date_order = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return str(self.id)
    
#     #метод-свойство (@property), который вычисляет и возвращает общую стоимость всех товаров в заказе. 
#     #Он получает все связанные объекты OrderItem для данного заказа и суммирует их стоимость.
#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
    
#     #метод-свойство (@property), который вычисляет и возвращает общее количество товаров в заказе. 
#     #Он получает все связанные объекты OrderItem для данного заказа и суммирует их количество.
#     @property
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.quantity for item in orderitems])
#         return total

# class ShippingAddres(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)
#     date_added = models.CharField(max_length=200, null=False)

#     def __str__(self):
#         return self.address
