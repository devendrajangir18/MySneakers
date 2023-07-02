from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField() 
    desc = models.TextField(max_length=220, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# makemigrations - create changes and store in a file
# migrate - apply the panding changes created by makemigrations

