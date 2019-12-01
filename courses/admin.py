from django.contrib import admin
from .models import Course, Announcement, Comment

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']

admin.site.register(Course, CourseAdmin)
admin.site.register([Announcement, Comment])