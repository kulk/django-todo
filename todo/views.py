from django.shortcuts import render
from .models import Task

#@login_required
def index(request):
	tasks = Task.objects.all()#author=request.user
	return render(request, 'todo/index.html', {'tasks': tasks})
