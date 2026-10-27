from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from college.serializers import Teacher_serializer,Student_serializer
from college.models import TeacherDB,StudentDB

# Create your views here.
class TeacherListCreateView(APIView):
    def get(self,request):
        qs=TeacherDB.objects.all()
        serializer_instance=Teacher_serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=Teacher_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TeacherRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(TeacherDB,id=pk)
        serializer_instance=Teacher_serializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        teacher_object=get_object_or_404(TeacherDB,id=pk)
        serializer_instance=Teacher_serializer(data=form_data, instance=teacher_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        teacher_object=get_object_or_404(TeacherDB, id=pk)
        teacher_object.delete()
        return Response(data={"Message":"Deleted.."})

class StudentListCreateView(APIView):
    def get(self,request):
        qs=StudentDB.objects.all()
        serializer_instance=Student_serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    