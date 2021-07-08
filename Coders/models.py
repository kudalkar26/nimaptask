from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Project(models.Model):
    Project= models.CharField(max_length= 60)


    def __str__(self):
        return self.Project


class Client(models.Model):
    client_name = models.CharField(max_length=255)

    created_by = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add= False, auto_now= False, blank=True)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)



    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})

    
    


    
