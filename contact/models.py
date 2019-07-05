from django.db import models

# Create your models here.

class ContactApply(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(null=True)
	course = models.CharField(verbose_name='Курс', max_length=20, default='Бачата', choices = (('s', 'Сальса casino'), ('b', 'Бачата')))
	message = models.CharField(max_length=510)
	subscribe = models.BooleanField()
	comment = models.TextField()
	is_active = models.BooleanField(default=True)
	date_apply = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name