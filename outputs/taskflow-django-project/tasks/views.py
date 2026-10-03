from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import SignUpForm, TaskForm
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if status in Task.Status.values:
        tasks = tasks.filter(status=status)
    all_tasks = Task.objects.filter(owner=request.user)
    return render(request, "tasks/task_list.html", {
        "tasks": tasks, "query": query, "selected_status": status,
        "total_count": all_tasks.count(), "todo_count": all_tasks.filter(status=Task.Status.TODO).count(),
        "progress_count": all_tasks.filter(status=Task.Status.IN_PROGRESS).count(),
        "done_count": all_tasks.filter(status=Task.Status.DONE).count(),
    })


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        messages.success(request, "Task created.")
        return redirect("task-list")
    return render(request, "tasks/task_form.html", {"form": form, "heading": "Create a task"})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your changes have been saved.")
        return redirect("task-list")
    return render(request, "tasks/task_form.html", {"form": form, "heading": "Edit task", "task": task})


@login_required
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect("task-list")


@login_required
@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.status = Task.Status.DONE if task.status != Task.Status.DONE else Task.Status.TODO
    task.save(update_fields=["status", "updated_at"])
    return redirect("task-list")


def signup(request):
    if request.user.is_authenticated:
        return redirect("task-list")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("task-list")
    return render(request, "registration/signup.html", {"form": form})
