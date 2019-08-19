from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


class Bb(models.Model):
    KINDS = (
        ('Куплю', 'Куплю'),
        ('Продам', 'Продам'),
        ('Обменяю', 'Обменяю'),
    )
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар',validators=[validators.MinLengthValidator(2, message='Слишком маленькое название')])
    content = models.TextField(null=True, blank=True, verbose_name='Описание', unique=True, error_messages={'unique' : 'Такое описание уже используется'})
    price = models.FloatField(null=True, blank=True, verbose_name='Цена', validators=[validators.MaxValueValidator(9999999)], error_messages={'max_value' : 'Слишком большая цена'})
    published =  models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    kind = models.CharField(max_length=10, choices=KINDS, blank=True, verbose_name='Действие')

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')
        if self.price < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение цены')
        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'объявление'
        ordering = ['-published']

    def title_and_price(self):
        if self.price:
            return '%s' '  ' '%d' % (self.title, self.price)
        else:
            return self.title
        title_and_price.short_description = 'Название и цена'

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']



# Create your models here.
