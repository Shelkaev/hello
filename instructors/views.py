from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor
from django.views.generic import DeleteView
from django.views.generic import ListView
# Create your views here.

class InstructorListView(ListView):
	model = Instructor
	template_name = 'instructors.html'
	context_object_name = 'instructors_list'

def instructors_list(request):
	instructors = Instructor.objects.all()
	return render (request, 'instructors.html', {'instructors_list':instructors})
	
class InstructorDetailView(DeleteView):
	model = Instructor
	template_name = 'personal_ins.html'
	pk_url_kwarg = 'instructor_id'
	context_object_name = 'personal_ins'


def sum_two(request, a, b):
	s = int(a) + int(b)
	return HttpResponse(s) 
	