from django.shortcuts import render
from django.views.generic import ListView, CreateView,DeleteView,UpdateView
from .models import Student
from .forms import StudentForm
# Create your views here.
# def hello(request):
#     return render(request, 'base.html')

class StudentListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['soni'] = Student.objects.all().count()
        context['studen'] = Student.objects.filter(id=2)

        return 

class StudentCreateView(CreateView):
    form_class = StudentForm 
    template_name = 's_create.html'
    success_url = '/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 's_delete.html'
    context_object_name = 'student'
    success_url = '/'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 's_update.html'
    fields = ['name', 'l_name']
    context_object_name = 'talaba'
    success_url = '/'