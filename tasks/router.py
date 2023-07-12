from rest_framework import routers

from tasks.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns_tasks = router.urls