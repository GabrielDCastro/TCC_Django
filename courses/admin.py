from django.contrib import admin
from .models import Course, Announcement, Comment, Turma


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin)
admin.site.register(Turma)
admin.site.register([Announcement, Comment])