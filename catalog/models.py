from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import datetime

class TouristProductEthap (models.Model):
    title = models.CharField (max_length = 200, verbose_name = "Название", help_text = "Введите короткое название вашего этапа")
    description = models.TextField ( max_length = 2000, verbose_name = "Описание", help_text = "Введите описание вашего этапа. Укажите чего стоит ожидать посетителям, сколько это займет по времени и как вы собираетесь проводить время на этом этапе." )
    image = models.ImageField(upload_to = "img/ethaps/", verbose_name = "Загрузите фотографию", help_text = "Загрузите фотографию данного этапа")
    place = models.ForeignKey ("Place", verbose_name = "Ссылка на объект", on_delete = models.SET_NULL, null = True, help_text = "Найдите это место в базе сайта. Если такового нет, оставьте это поле пустым")
    creator = models.ForeignKey (to = User, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return str( self.title )


class TouristProduct (models.Model):
    title = models.CharField (max_length = 200, verbose_name = "Название", help_text = "Введите короткое название вашего туристического продукта")
    description = models.TextField (max_length  = 1000, blank = True, verbose_name = "Описание", help_text = "Введите описание вашего этапа. Укажите чего стоит ожидать покупателям, сколько это займет по времени и что им стоит взять с собой.")
    creator = models.ForeignKey (to = User, on_delete = models.SET_NULL, null=True)
    price = models.DecimalField (max_digits = 8, decimal_places = 2, verbose_name = "Цена")
    headerImage = models.ImageField(upload_to = "img/tours/", verbose_name = "Главная фотография")
    ethaps = models.ManyToManyField ( to = TouristProductEthap )
    timeWillTake = models.TimeField( auto_now = False, verbose_name = "Время:", null = True)

    def getEthaps (self):
        return self.ethaps.all()

    def getAbsoluteUrl(self):
        return reverse("productDetails", args=[str(self.id)])

    def __str__(self):
        return str (self.title)

class TouristProductInstance (models.Model):
    TouristProduct = models.ForeignKey ( to = TouristProduct, on_delete = models.CASCADE )

class Place (models.Model):
    title = models.CharField ( max_length = 200 )
    description = models.TextField ( max_length = 3000, help_text = "" )
    image = models.ImageField(upload_to = "img/places/", help_text = "Загрузите фотографию данного этапа")
    owner = models.ForeignKey ( to = User, on_delete = models.SET_NULL, null = True )
    
    def __str__(self):
        return self.title

    def getAbsoluteUrl(self):
        return reverse("placeDetail", args=[str(self.id)])

RATE_CHOISES = [
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Удовлетворительно"),
        (4, "Хорошо"),
        (5, "Отлично"),
        ]

class Review (models.Model):
    touristProduct = models.ForeignKey ( to = TouristProduct, on_delete = models.CASCADE)
    comment = models.TextField (max_length = 1000)
    rate = models.PositiveSmallIntegerField( choices=RATE_CHOISES )
    user = models.ForeignKey (User, on_delete = models.CASCADE)
    date = models.DateField( auto_now_add=True, null = False )
    likes = models.PositiveIntegerField ( default = 0 )
    dislikes = models.PositiveIntegerField ( default = 0 )

    def __str__ (self):
        return f"{self.comment} | {self.user.first_name} {self.user.last_name}"
