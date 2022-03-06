from django.shortcuts import render
from myapp.models import Student
from myapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

#Model object - Single Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    student_serilizer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(student_serilizer.data)

    # return  HttpResponse(json_data,content_type='application/json')

    return JsonResponse(student_serilizer.data,)

