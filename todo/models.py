from django.db import models

# Create your models here.
 
class Task(models.Model):
    task = models.CharField(max_length=255)  # Task name
    Iscompleted = models.BooleanField(default=False)  # Completion status
    created_at = models.DateTimeField(auto_now=True)  # Default to current time

    def __str__(self):
        return self.task

