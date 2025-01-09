from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    """
    A view to display tasks to do and completed tasks with 
    tasks due first at the top and completed tasks at the bottom
    """
    to_do_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')

    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks,
    }   
    return render(request, 'tasks/index.html', context)