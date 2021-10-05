from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.rutas.models import Ciudad, Trayecto
from apps.rutas.api.serializers import CiudadSerializer, TrayectoSerializer


@api_view(['GET'])
def get_ciudad_api_view(request):
    if request.method == 'GET':
        ciudades = Ciudad.objects.all()
        ciudades_serializer = CiudadSerializer(ciudades, many=True)
        return Response(ciudades_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_ciudad_by_id_api_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            ciudad = Ciudad.objects.filter(id=pk).first()
            if ciudad:
                ciudad_serializer = CiudadSerializer(ciudad)
                return Response(ciudad_serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'No se ha encontrado una ciudad con ese id'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_trayecto_by_id_api_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            trayecto = Trayecto.objects.filter(id=pk).first()
            if trayecto:
                trayecto_serializer = TrayectoSerializer(trayecto)
                return Response(trayecto_serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'No se ha encontrado un trayecto con ese id'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_trayecto_api_view(request):
    if request.method == 'GET':
        trayectos = Trayecto.objects.all()
        trayectos_serializer = TrayectoSerializer(trayectos, many=True)
        return Response(trayectos_serializer.data, status=status.HTTP_200_OK)