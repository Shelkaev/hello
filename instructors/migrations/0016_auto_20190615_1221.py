# Generated by Django 2.1.7 on 2019-06-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0015_instructor_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(help_text='Загрузите фотографию', null=True, upload_to='', verbose_name='Имя'),
        ),
    ]
