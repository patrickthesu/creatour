# Generated by Django 4.1.5 on 2023-01-29 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('image', models.ImageField(help_text='Загрузите фотографию данного этапа', upload_to='img/places/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TouristProductEthap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите короткое название вашего этапа', max_length=200, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание вашего этапа. Укажите чего стоит ожидать посетителям, сколько это займет по времени и как вы собираетесь проводить время на этом этапе.', max_length=2000, verbose_name='Описание')),
                ('image', models.ImageField(help_text='Загрузите фотографию данного этапа', upload_to='img/ethaps/', verbose_name='Загрузите фотографию')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(help_text='Найдите это место в базе сайта. Если такового нет, оставьте это поле пустым', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.place', verbose_name='Ссылка на объект')),
            ],
        ),
        migrations.CreateModel(
            name='TouristProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите короткое название вашего туристического продукта', max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Введите описание вашего этапа. Укажите чего стоит ожидать покупателям, сколько это займет по времени и что им стоит взять с собой.', max_length=1000, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('headerImage', models.ImageField(upload_to='img/tours/', verbose_name='Главная фотография')),
                ('timeWillTake', models.TimeField(null=True, verbose_name='Времея:')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ethaps', models.ManyToManyField(to='catalog.touristproductethap')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Ужасно'), (2, 'Плохо'), (3, 'Удовлетворительно'), (4, 'Хорошо'), (5, 'Отлично')])),
                ('date', models.DateField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('touristProduct', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.touristproduct')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]