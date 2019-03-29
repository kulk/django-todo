from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

@login_required
def index(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.user = request.user
			task.save()
			return redirect('index')
	else:
		form = TaskForm()
	tasks = Task.objects.filter(user=request.user)
	return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})

@login_required
def delete(request, pk):
	task = get_object_or_404(Task, pk=pk)
	task.delete()
	return redirect('index')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'todo/register.html', {'form': form})
	