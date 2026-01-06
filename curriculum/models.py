from django.db import models
from courses.models import Course
# Create your models here.

class Lesson(models.Model):
    course=models.ForeignKey(Course, blank=False, on_delete=models.CASCADE)
    video= models.URLField(blank=True)
    order= models.PositiveIntegerField(default=1)
    topic = models.CharField(max_length=120)
    duration = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['order']

    def __str__(self):
        return self.topic