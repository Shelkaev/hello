from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

class Position(models.Model):
	name = models.CharField(null=True, max_length=225)
	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(null=True, max_length=225)
	def __str__(self):
		return self.name

class Instructor(models.Model):
	photo = models.ImageField(verbose_name='Имя', null=True, max_length=100, help_text = 'Загрузите фотографию')
	name = models.CharField(verbose_name='Имя', max_length=255, help_text = 'Введите имя')
	surname = models.CharField(verbose_name='Фамилия', max_length=225)
	gender = models.CharField(verbose_name='Пол', null=True, blank=True, max_length=1, choices = (('М', 'Мужчина'), ('Ж', 'Женщина')))
	course = models.ManyToManyField(Course, verbose_name='Курс')
	date_of_birth = models.DateField(null=True, blank=True)
	emaill = models.EmailField(unique=True, null=True)
	is_active = models.BooleanField(default=True)
	position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
	description = models.TextField(null=True, blank=True, help_text = 'В данное поле вводится краткая биография и основные черты личности', verbose_name='О себе')
	phone = models.CharField(max_length = 15, null=True, blank=True)
	def __str__(self):
		return self.name
		
			
	
	'''
	phone = models.CharField(max_length = 15, null=True, blank=True)
	slug = models.SlugField(unique=True)
	gender = models.CharField(max_length=1, choices = (('m', 'Male'), ('f', 'Female')))
	'''