from django.contrib import admin
from instructors.models import Instructor, Position, Course
from django.db import models
from django.forms import widgets

class InstructorInline(admin.StackedInline):
	model = Instructor
	fields = ['name']

class PositionAdmin(admin.ModelAdmin):
	inlines = [InstructorInline]

class InstructorAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname','is_active', 'position']
	list_display_link = ['name', 'surname']
	list_filter = ['is_active', 'position', 'course']
	search_fields = ['name', 'surname']
	list_editable = ['is_active']
	#fields = ['name', 'surname', 'emaill','date_of_birth', 'position','is_active']
	#exclude = ['date_of_birth']
	readonly_fields = ['is_active']
	raw_id_fields = ['position']
	
	save_as = False
	save_on_top = False
	
	fieldsets = (
		(None, {
            'fields': ('photo', 'name', 'surname', 'course')
        }),
        ('Date informations', {
            'classes': ('collapse',),
            'fields': ('emaill', 'phone', 'gender', 'date_of_birth', 'position','is_active', 'description'),
        }),
    )
	formfield_overrides = {
		models.DateField: { 'widget': widgets.TextInput}
	}
	
# Register your models here.
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Course)