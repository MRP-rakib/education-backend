from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses_images/image/', null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    total_lessons = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    category = models.CharField(max_length=120)
    language = models.CharField(max_length=120)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username}-{self.course.title}({self.rating})"

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.course.title}"
