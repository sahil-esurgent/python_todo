"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from . import views
from .api import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Todoslist', TodoViewSet, basename="TodoList")


urlpatterns = [
    path("api/", include(router.urls)),
    path('', views.apiOverview, name='api_overview'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo_detail/<int:pk>', views.todo_detail, name='todo_detail'),
    path('todo_create/', views.todo_create, name='todo_create'),
    path('todo_edit/<int:pk>', views.todo_edit, name='todo_edit'),
    # path('todo_update/', views.todo_update, name='todo_update'),
    path('todo_update/<int:pk>', views.todo_update, name='todo_update'),
    # path('todo_status/<int:pk>', views.todo_status, name='todo_status'),
    path('todo_delete/<int:pk>', views.todo_delete, name='todo_delete'),
]
