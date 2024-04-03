from django.shortcuts import render
from core.models import Student

# Create your views here.
def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'core/index.html', context)