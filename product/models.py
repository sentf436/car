from django.db import models


class Category(models.Model):
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField(primary_key=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=90, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cate', verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
