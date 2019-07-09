from django.shortcuts import render
from django import forms
from django.views.generic.edit import FormView
from main.models import EmailMessage
from django.contrib import messages

# Create your views here.

class EmailMessageForm(forms.ModelForm):
	class Meta:
		model = EmailMessage
		exclude = ['date_apply', 'is_active', 'comment']
		widgets = {'message' : forms.Textarea}

class IndexViewForm(FormView):
	form_class = EmailMessageForm
	template_name = 'index.html'
	success_url = '/'
	
	def form_valid(self, form):
		message = form.save()
		messages.success(self.request, 'Сообщение отправлено')
		return super().form_valid(form)
	
	"""prefix = 'emaill_message'
	placeholder = 'Мобильный телефон или email'
	initial = {'placeholder': placeholder}"""


"""def index(request):
	context = {'var1': 'Привет мир!'}
	context['var2'] = {'some_str': 'Привет питон!'}
	context['var3'] = ['a', 'b', 'c']
	return render (request, 'index.html', context)"""
	
"""	def form_valid(self, form):
		message = form.save()
		messages.success(request, 'Сообщение отправлено')"""