# Generated by Django 2.1.7 on 2019-06-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0012_auto_20190610_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='description',
            field=models.TextField(blank=True, help_text='В данное поле вводится краткая биография и основные черты личности', null=True, verbose_name='О себе'),
        ),
    ]
