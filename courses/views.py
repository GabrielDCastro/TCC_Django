from django.shortcuts import render
from .models import Course, Announcement, Turma

'''
from django.shortcuts import get_object_or_404, redirect
from .models import Enrollment
from django.contrib.auth.decorators import login_required
'''

def cursos(request):
    courses = Turma.objects.all()
    template_name = 'courses/cursos.html'
    context = {
        'courses': courses,
    }
    return render (request, template_name, context)

def details(request, pk):
    course = Turma.objects.get(pk=pk)
    context ={
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)

def announcements(request):
    course = request.course
    template = 'courses/announcements.html'
    context = {
        'course': course,
        'announcements': course.announcements.all()
    }
    return render(request, template, context)


def lessons(requests, slug):
    course = requests.course
    template = 'courses/lessons.html'
    context = {
        'course': course
    }
    return render(requests, template, context)
'''
@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    #if created:
    #   enrollment.active()
    return redirect('accounts:dashboard')
'''