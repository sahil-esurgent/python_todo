from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save()

    # @action(methods=['get'], detail=True, url_path='todo_list', url_name='todo_list')
    # def todo_list(self, request):
    #     return self.queryset
    
    # @action(methods=['get'], detail=True, url_path='todo_detail', url_name='todo_detail')
    # def todo_detail(self, request,pk=None):
    #     todos = get_object_or_404(self.queryset, pk=pk)
    #     serializer = TodoSerializer(todos)
    #     return Response(serializer.data)
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data)
