from tourtoken_webapp.entry.models import Entry
from tourtoken_webapp.entry.serializers import EntrySerializer
from rest_framework import generics


class EntryListCreate(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
