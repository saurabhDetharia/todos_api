from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TodoViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
