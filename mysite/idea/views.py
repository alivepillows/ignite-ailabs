# views.py
from rest_framework import viewsets
from .models import Ide
from .serializers import IdeSerializer

class IdeViewSet(viewsets.ModelViewSet):
    queryset = Ide.objects.all()
    serializer_class = IdeSerializer
