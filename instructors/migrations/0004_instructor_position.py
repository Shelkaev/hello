# Generated by Django 2.1.7 on 2019-06-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_instructor_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='position',
            field=models.CharField(choices=[('i', 'Instructor'), ('a', 'Assistent')], max_length=1, null=True),
        ),
    ]
