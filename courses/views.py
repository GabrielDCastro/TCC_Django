from django.shortcuts import render
from .models import Course

def cursos(request):
    courses = Course.objects.all()
    template_name = 'courses/cursos.html'
    context = {
        'courses': courses
    }
    return render (request, template_name, context)
