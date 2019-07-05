from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from students.models import Students

class StudentsAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname', 'side']

# Register your models here.

#class ImageWidget(AdminFileWidget):


admin.site.register(Students, StudentsAdmin)