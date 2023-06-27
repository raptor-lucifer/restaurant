from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number_of_person=models.IntegerField()
    special_request=models.TextField()
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.name
    