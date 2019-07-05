# Generated by Django 2.1.7 on 2019-06-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20190606_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату в формате ГГГГ-ММ-ДД', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='students',
            name='surname',
            field=models.CharField(blank=True, help_text='Введите фамилию', max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]
