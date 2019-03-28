from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	timestamp = models.DateTimeField(default=timezone.now)