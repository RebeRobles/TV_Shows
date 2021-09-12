from django.db import models
from .models import *

# Create your models here.


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return self.title
