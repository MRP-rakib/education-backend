from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from curriculum.models import Lesson
from instructors.models import Instructor
from courses.serializers import CourseSerializer,CourseCreateSerializer
from instructors.serializer import InstructorSerializer
from curriculum.serializer import LessonSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializer import BlogSerializer



class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CourseCreateSerializer
        return CourseSerializer
    @action(detail=True, methods=['get'])
    def suggestions(self, request, pk=None):
        course = self.get_object()
        suggestions = Course.objects.filter(
            category=course.category
        ).exclude(id=course.id)

        serializer = CourseSerializer(suggestions, many=True)
        return Response(serializer.data)
    



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer