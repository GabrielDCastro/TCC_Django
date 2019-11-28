from django.shortcuts import render ''', get_object_or_404, redirect'''
from .models import Course ''', Enrollment
from django.contrib.auth.decorators import login_required'''

def cursos(request):
    courses = Course.objects.all()
    template_name = 'courses/cursos.html'
    context = {
        'courses': courses
    }
    return render (request, template_name, context)

def details(request, pk):
    course = Course.objects.get(pk=pk)
    context ={
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)

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