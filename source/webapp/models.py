from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

CATEGORIES_CHOICES = [("other", "Разное"), ("electronics", "Электроника"), ("books", "Книги"),
                      ("stationery", "Канцтовары")]
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    category = models.CharField(max_length=255, blank=False, choices=CATEGORIES_CHOICES, default=CATEGORIES_CHOICES[0][0], verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, verbose_name='Картинка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='products')

    def get_rating(self):

        return 4.5


    def __str__(self):
        return f'{self.pk}. {self.name}'

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    review_text = models.TextField(max_length=2000, blank=False, verbose_name='Текст отзыва')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, verbose_name='Оценка')
    is_reviewed = models.BooleanField(default=False, verbose_name='С отзывом')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.pk}. {self.author}'