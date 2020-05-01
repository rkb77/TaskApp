from django.shortcuts import render, redirect
from django.http import HttpResponse
from Task_App.models import TaskList
from Task_App.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'index_text':'Welcome index page.',
    }
    return render(request, 'home.html', context)

def contact(request):
    context = {
        'contact_text':'Welcome contact-us page.',
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':'Welcome about-us page.',
    }
    return render(request, 'about.html', context)

@login_required
def taskapp(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request, ('Task add Successfully'))
        return redirect('task')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'taskapp.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        return redirect('task')

@login_required
def edit_task(request, task_id):
    if request.method=="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ('Task edited Successfully'))
        return redirect('task')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edittask.html', {'task_obj': task_obj})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
        messages.success(request, ('Task Completed'))
    else:
        messages.success(request, ('Access is denied'))
    return redirect('task')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    messages.success(request, ('Task Pending'))
    return redirect('task')
