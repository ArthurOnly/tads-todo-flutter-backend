
from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description')

class TaskSyncSerializer(serializers.Serializer):
    tasks = TaskSerializer(many=True)

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        for task in tasks:
            exists = Task.objects.filter(title=task.get("title")).exists()
            if not exists:
                Task.objects.create(**task)
        return tasks

