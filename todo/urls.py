from django.contrib import admin
from .views import todo_list_create

urlpatterns = [
    path('list-create/', todo_list_create)
    
]
