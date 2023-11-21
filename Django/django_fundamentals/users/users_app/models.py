from django.db import models

class users(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email_address= models.TextField()
    age= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
