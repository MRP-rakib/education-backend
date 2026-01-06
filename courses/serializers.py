from rest_framework import serializers
from .models import Course
from curriculum.serializer import LessonSerializer
from instructors.serializer import InstructorSerializer

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title','image','description','price','category','language']


class CourseSerializer(serializers.ModelSerializer):
    lessons=LessonSerializer(many=True,read_only=True,source='lesson_set')
    instructor = InstructorSerializer(many=True, read_only=True, source='instructor_set')
    class Meta:
        model = Course
        fields = '__all__'