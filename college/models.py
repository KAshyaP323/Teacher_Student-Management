from django.db import models

# Create your models here.
class TeacherDB(models.Model):
    name=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    subject=models.CharField(max_length=100)
    college=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class StudentDB(models.Model):
    name=models.CharField(max_length=200)
    teacher_id=models.IntegerField()
    batch=models.CharField(max_length=100)
    year=models.PositiveIntegerField()

    def __str__(self):
        return self.name