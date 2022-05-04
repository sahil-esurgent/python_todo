from urllib import request
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
        'List' : '/Todo-list/',
        'Detail View' : '/Todo-detail/<int:pk>/',
        'Create' : '/Todo-create/',
        'Update' : '/Todo-update/<int:pk>/',
        'Delete' : '/Todo-delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def todo_list(requset, format=None):
    
    # renderer_classes = [TemplateHTMLRenderer]

    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    all_data = serializer.data
    return Response({'todos': all_data}, template_name = 'todo_app/todo.html')

@api_view(['GET'])
def todo_detail(requset,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def todo_create(requset):
    serializer = TodoSerializer(data=requset.data)
    if serializer.is_valid():
        serializer.save()
    # return Response(serializer.data)
    todos = Todo.objects.all()
    serializer1 = TodoSerializer(todos, many=True)
    all_data = serializer1.data
    return Response({'todos': all_data}, template_name = 'todo_app/todo.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def todo_edit(requset,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos)
    todo = serializer.data
    return Response({'todos': todo}, template_name = 'todo_app/todo_edit.html')

@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def todo_update(request,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    # return Response(serializer.data)
    todos = Todo.objects.all()
    serializer1 = TodoSerializer(todos, many=True)
    all_data = serializer1.data
    return Response({'todos': all_data}, template_name = 'todo_app/todo.html')

@api_view(['DELETE'])
# @renderer_classes([TemplateHTMLRenderer])
def todo_delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect(todo_list)
    # return Response("Todo Task Deleted Successfully...")
    # todos = Todo.objects.all()
    # serializer = TodoSerializer(todos, many=True)
    # all_data = serializer.data
    # return Response({'todos': all_data}, template_name = 'todo_app/todo.html')

# @api_view(['put'])
# @renderer_classes([TemplateHTMLRenderer])
# def todo_status(request,pk):
#     print(request)
#     todo = Todo.objects.get(id=pk)
#     print("Todo --------------> ",todo.id)
#     data = {
#         'title' : todo.title,
#         'date'  : todo.date,
#         'status' : "Completed"
#     }
#     serializer = TodoSerializer(instance=todo, data=data)
#     if serializer.is_valid():
#         serializer.save()
#     todos = Todo.objects.all()
#     serializer1 = TodoSerializer(todos, many=True)
#     all_data = serializer1.data
#     return Response({'todos': all_data}, template_name = 'todo_app/todo.html')