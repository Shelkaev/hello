from django.shortcuts import render

# Create your views here.

def index(request):
	context = {'var1': 'Привет мир!'}
	context['var2'] = {'some_str': 'Привет питон!'}
	context['var3'] = ['a', 'b', 'c']
	return render (request, 'index.html', context)