from django.db import models

# Create your models here.
class Todo(models.Model):
    data = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)