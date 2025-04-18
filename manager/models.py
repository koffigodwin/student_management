from django.db import models

# Create your models here.
class Students(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=50)
    cgpa = models.FloatField()

    def __str__(self):
        return f"Studend {self.first_name} {self.last_name}"