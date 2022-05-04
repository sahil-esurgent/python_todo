from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)
    status = models.CharField(max_length=20, default="Pending", blank=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.title