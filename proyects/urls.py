from rest_framework import routers
from .api import ProyectViewSet

rauter = routers.DefaultRouter()

rauter.register('api/proyects', ProyectViewSet, 'proyect')
