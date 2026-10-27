from rest_framework import serializers
from college.models import TeacherDB,StudentDB

class Teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherDB
        fields="__all__"
        read_only_fields=["id"]

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDB
        fields="__all__"
        read_only_fields=["id"]