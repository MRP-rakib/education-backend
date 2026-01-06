from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Lesson
from courses.models import Course

@receiver(post_save,sender=Lesson)
def update_total_lessons_on_save(sender,instance,**kwargs):
    course = instance.course
    if course:
        course.total_lessons=course.lesson_set.count()
        course.total_hours = sum(l.duration for l in course.lesson_set.all())
        course.save()

@receiver(post_delete, sender=Lesson)
def update_total_lessons_on_delete(sender, instance, **kwargs):
    course = instance.course
    if course:
        course.total_lessons = course.lesson_set.count()
        course.total_hours = sum(l.duration for l in course.lesson_set.all())
        course.save()

