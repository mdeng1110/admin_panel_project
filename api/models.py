from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description", max_length=2000)
    created = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=True)
    instructor = models.ForeignKey(Instructor, related_name="courses", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
