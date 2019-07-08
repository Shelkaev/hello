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

	def get_queryset(self):
		qs = super().get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(course__id = course_id)
		return qs
	
class InstructorDetailView(DeleteView):
	model = Instructor
	template_name = 'personal_ins.html'
	pk_url_kwarg = 'instructor_id'
	context_object_name = 'personal_ins'


def sum_two(request, a, b):
	s = int(a) + int(b)
	return HttpResponse(s) 
	