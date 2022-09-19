from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL - адрес категории', blank=True)  # Что такое slug?

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    sub_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Подкатегория товаров')
    sub_name = models.CharField(max_length=200, db_index=True, verbose_name='Название подкатегории')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.sub_name



class Product(models.Model):
    product_category = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE,  verbose_name='Категория товаров')
    product_name = models.CharField(max_length=200, db_index=True,  verbose_name='Название продукта')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL - адрес продукта')
    product_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,  verbose_name='Изображение продукта')
    product_description = models.TextField(blank=True,  verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='Цена за штуку')
    stock = models.PositiveIntegerField(verbose_name='Количество продуктов ')
    available = models.BooleanField(default=True, verbose_name='Есть в наличии!')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания продукта')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время добавления продукта')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.product_name

