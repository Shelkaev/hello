# Generated by Django 2.1.7 on 2019-06-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190606_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(help_text='Введите имя', max_length=50, null=True, verbose_name='Имя'),
        ),
    ]
