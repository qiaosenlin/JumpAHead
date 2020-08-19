from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .models import Module
from .models import Task
from .forms import checkCompleteTaskForm
from django.http import JsonResponse, QueryDict, HttpResponse






from django.utils import timezone
from django.views.generic.detail import DetailView, BaseDetailView



# Create your views here.

def moduleList(request):
    if(not request.user.is_authenticated):
        return redirect('home')
    # Get all modules from database
    queryset = Course.objects.all()
    tasks = Task.objects.all()
    # Create course dict with modules
    courses = sorted(queryset, key=lambda x: x.title, reverse=False)
    context = {
        "courses":courses,
        "tasks": tasks
    }
    return render(request,"moduleList.html",context)


class ModuleDetailView(DetailView):
    model = Module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tasks'] = self.get_object().tasks.all().order_by('description')
        form = checkCompleteTaskForm()
        context['form'] = form
        return context

def isCompleteView(request):
    if request.method == "POST":
        data =request.POST
        num = data.get('number')
        print(data)
        data = Task.objects.get(id=num)
        checkComplete = data.checkComplete
        form = checkCompleteTaskForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
        return HttpResponse()
    else:
        return JsonResponse({"success":False}, status=400)
