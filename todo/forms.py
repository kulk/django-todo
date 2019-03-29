from django import forms
from . models import Task

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('body',)
		'''
		labels = {
            'body': ('Enter task '), # Create a custom label for the field 'body'
        }
		'''