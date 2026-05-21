from django.shortcuts import render
from .models import Notes
from .serializer import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import(
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

)

# Create your views here.
# with generic
class ListCreateNotes(ListCreateAPIView):
    queryset=Notes.objects.all()
    serializer_class= NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DetailNotes(RetrieveUpdateDestroyAPIView):
    queryset=Notes.objects.all()
    serializer_class= NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)



