from django.db import models


# Create your models here.
class djangoClass(models.Model):
    Title = models.CharField(max_length=100)
    CourseNumber = models.IntegerField(max_length=5)
    InstructorName = models.CharField(max_length=50)
    Duration = models.FloatField(max_length=5)

    djangoClasses = models.Manager()

    def __str__(self):
        return self.Title



