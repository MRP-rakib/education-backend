from django.db import models

class Blog(models.Model):

    CATEGORY_CHOICES = (
        ('education', 'Education'),
        ('course', 'Online Course'),
        ('career', 'Career'),
    )

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
