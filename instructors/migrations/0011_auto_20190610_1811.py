# Generated by Django 2.1.7 on 2019-06-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0010_auto_20190610_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(help_text='Загрузите фотографию', null=True, upload_to='media/', verbose_name='Фото'),
        ),
    ]
