# Inside your app's models.py file
from django.db import models
import re  # Import the regex module

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['Title']) < 2:
            errors["Title"] = "Blog name should be at least 5 characters"
        # else: len(postData['network']) < 2:
        #     errors["Title"] = "Blog name should be at least 5 characters"
        # else: len(postData['Title']) < 2:
        #     errors[""] = "Blog name should be at least 5 characters"
        


        return errors

class Show(models.Model):
    Title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
    

