from rest_framework import viewsets
from api.models import Note
from api.serializer import NoteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
