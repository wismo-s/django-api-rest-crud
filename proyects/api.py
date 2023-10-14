from .models import Proyect
from rest_framework import viewsets, permissions
from .serializers import ProyectSerializers

class ProyectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerializers