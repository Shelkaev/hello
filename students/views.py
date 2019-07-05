from django.shortcuts import render, get_object_or_404
from students.models import Students
# Create your views here.

def students_list(request):
	students = Students.objects.all()
	return render (request, 'students.html', {'students_list':students})
	
def personal_stud(request, students_id):
	person = get_object_or_404(Students, pk=students_id)
	return render (request, 'personal_stud.html', {'personal_stud':person})