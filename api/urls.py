from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, InstructorViewSet , BlogViewSet
from contact.views import ContactViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('instructors', InstructorViewSet)
router.register('blogs',BlogViewSet)
router.register('contact',ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
