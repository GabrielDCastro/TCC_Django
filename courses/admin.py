from django.contrib import admin
from .models import Course, Turma


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin)
admin.site.register(Turma)