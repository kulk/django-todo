from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

#@login_required
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
	tasks = Task.objects.all()
	return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})
