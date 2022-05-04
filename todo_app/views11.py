from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/todo_list/',
        'Detail View' : '/todo_detail/<int:pk>/',
        'Create' : '/todo_create/',
        'Update' : '/todo_update/<int:pk>/',
        'Delete' : '/todo_delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def todo_list(requset):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(requset,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos)
    return Response(serializer.data)

@api_view(['POST'])
def todo_create(requset):
    serializer = TodoSerializer(data=requset.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def todo_update(requset,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todos, data=requset.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todo_delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Todo Task Deleted Successfully...")