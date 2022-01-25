from functools import partial
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = studentSerializer(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return Response(serializer.data)


@api_view(['GET'])
def students(request):
    student = Student.objects.all()
    serializer = studentSerializer(student, many=True)
    return Response(serializer.data)


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@api_view(['PUT'])
def update(request, pk):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    student = Student.objects.get(id=pk)
    serializer = studentSerializer(student, data=pythondata, partial=True)
    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Updated!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')


@api_view(['DELETE'])
def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    res = {'msg': 'Data deleted!'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')
