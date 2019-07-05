# Generated by Django 2.1.7 on 2019-06-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0011_auto_20190610_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='simbols',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='course',
            field=models.ManyToManyField(to='instructors.Course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(help_text='Введите имя', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(help_text='Загрузите фотографию', null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='surname',
            field=models.CharField(max_length=225, verbose_name='Фамилия'),
        ),
    ]
