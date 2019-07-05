from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor
# Create your views here.

def instructors_list(request):
	instructors = Instructor.objects.all()
	return render (request, 'instructors.html', {'instructors_list':instructors})
	
def personal_ins(request, instructor_id):
	person = get_object_or_404(Instructor, pk=instructor_id)
	return render (request, 'personal_ins.html', {'personal_ins':person})

def sum_two(request, a, b):
	s = int(a) + int(b)
	return HttpResponse(s) 
	