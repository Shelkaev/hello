from django.shortcuts import render, redirect
from django import forms
from contact.models import ContactApply
from django.contrib import messages

# Create your views here.

'''
class ContactForm(forms.Form):
	name = forms.CharField(max_length=20, initial= 'Григорий')
	email = forms.EmailField(label='Почта', help_text='это почта')
	course = forms.ChoiceField(choices = (('s', 'Сальса casino'), ('b', 'Бачата')))
	message = forms.CharField(max_length=510)
	subscribe = forms.BooleanField(required=False)
'''
	
class ModelContactForm(forms.ModelForm):
	class Meta:
		model = ContactApply
		exclude = ['date_apply', 'is_active', 'comment']
		#fields
		widgets = {'message' : forms.Textarea, 'course': forms.Select}
		labels = {'email': 'Mail'}

def contact(request):
	if request.method == 'POST':
		form = ModelContactForm(request.POST)
		if form.is_valid():
			instance = form.save()
			messages.success(request, 'Сообщение отправлено')
		return redirect(to=('/contact/'+str(instance.id)))
	else:
		form = ModelContactForm(initial={'course':'b', 'subscribe': True})
	return render (request, 'contact.html', {'form': form})
	
def contact_edit(request, contact_id):
	contactapply = ContactApply.objects.get(id=contact_id)
	if request.method == 'POST':
		form = ModelContactForm(request.POST, instance=contactapply)
		if form.is_valid():
			contactapply = form.save()
			messages.success(request, 'Сообщение от пользавателя ' + contactapply.name + '<br/>' + 'Адрес эл. почты: ' + contactapply.email + '<br/>' + 'успешно отредактировано.')
			return redirect(to = '/contact/')
	else:
		form = ModelContactForm(instance=contactapply)
	return render(request, 'contact_edit.html', {'form':form, 'contactapply' : contactapply})
	
def contact_delete(request, contact_id):
	contactapply = ContactApply.objects.get(id=contact_id)
	if request.method == 'POST':
		ms = 'Сообщение от пользавателя ' + contactapply.name + '<br/>' + 'Адрес эл. почты: ' + contactapply.email + '<br/>' + 'успешно удалено.'
		contactapply.delete()
		messages.success(request, ms)
		return redirect(to = '/contact/')

	return render(request, 'contact_delete.html', {'contactapply':contactapply})