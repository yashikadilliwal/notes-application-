
from django.urls import path
from .views import ListCreateNotes,DetailNotes

urlpatterns = [
    path('notes/', ListCreateNotes.as_view()),
    path('<int:pk>/', DetailNotes.as_view() ),
    
]
