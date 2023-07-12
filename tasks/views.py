from django.shortcuts import render
from requests import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskSyncSerializer
from rest_framework import status
from rest_framework.decorators import action

from rest_framework import viewsets

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['post'])
    def sync(self, request):
        serializer = TaskSyncSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)