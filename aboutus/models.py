from django.db import models

# Create your models here.


class Chef(models.Model):
    name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    image=models.ImageField(upload_to='chef/')

    def __str__(self):
        return self.name
    
