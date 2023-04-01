from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from tasks import views

# https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()

router.register(r"todo_lists", views.TodoListViewSet)
# router.register(r"todo_lists", views.TodoItemsViewSet)
router.register(r"todo_items", views.TodoItemViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
