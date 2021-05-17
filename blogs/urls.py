from django.urls import path
from .import views

urlpatterns = [
    path('blogs/', views.snippet_list),
    
]