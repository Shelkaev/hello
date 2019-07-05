from django.db import models
from instructors.models import Course, Instructor

# Create your models here.

class Students(models.Model):
	photo = models.ImageField(verbose_name='Фото', null=True, max_length=100, help_text = 'Загрузите фотографию')
	name = models.CharField(null=True, verbose_name='Имя', max_length=50, help_text = 'Введите имя')
	surname = models.CharField(null=True, blank=True, verbose_name='Фамилия', max_length=50, help_text = 'Введите фамилию')
	date_of_birth = models.DateField(null=True, verbose_name='Дата рождения', help_text = 'Введите дату в формате ГГГГ-ММ-ДД')
	side = models.ForeignKey('instructors.Course', on_delete=models.CASCADE, null=True, verbose_name='Программа подготовки')
	lider = models.ForeignKey('instructors.Instructor', on_delete=models.CASCADE, null=True, verbose_name='Руководитель')
	description = models.TextField(null=True, blank=True, help_text = 'В данное поле вводится краткая биография и основные черты личности', verbose_name='Описание')
	gender = models.CharField(verbose_name='Пол', null=True, blank=True, max_length=1, choices = (('М', 'Мужчина'), ('Ж', 'Женщина')))
	def __str__(self):
		return (self.name)