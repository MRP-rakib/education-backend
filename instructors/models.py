from django.db import models
from courses.models import Course
# Create your models here.
class Instructor(models.Model):
    course=models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    department = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='instructors_image/',blank=True,null=True)
    total_student = models.IntegerField()
    total_courses = models.IntegerField()
    facebook= models.URLField(blank=True,null=True)
    linkedin= models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name
    