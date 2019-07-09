from django.db import models

# Create your models here.


class EmailMessage(models.Model):
	email = models.CharField(null=True, max_length=50)
	comment = models.TextField()
	is_active = models.BooleanField(default=True)
	date_apply = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.email
	
	def send_email(self):
		# send email using the self.cleaned_data dictionary
		pass