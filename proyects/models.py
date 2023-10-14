from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=150)  
    description = models.TextField()
    technology =  models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)