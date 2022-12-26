from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from mundial_api.models import Equipo, Jugador
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EquipoSerializer
from .serializers import JugadorSerializer
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET'])
def listaEquipos(request):
    #Musicos.objects.all() => select * from musico;
    equipos= Equipo.objects.all()
    serializado = EquipoSerializer(equipos, many=True)
    return Response(serializado.data)

@api_view(['GET'])
#"@permission_classes([IsAuthenticated])
def mostrarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    serializado = JugadorSerializer(jugador)
    return Response(serializado.data)



@api_view(['POST', 'PATCH', 'DELETE'])
#@permission_classes([IsAuthenticated])
def gestionarJugador(request, id):
    #si deseo ingresar jugador
    if request.method == 'POST':
        try:
            serializador = JugadorSerializer(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            # no es valido el serializador se los datos recibidos
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    #si deseo modificar
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUE)

    # si deseo eliminar JUGADOR
    if request.method == 'DELETE':
        #hago eliminacion
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Por favor ingrese usuario y/o contraseña en conjunto'},
                        status=status.HTTP_400_BAD_REQUEST)
    # intentar hacer login con los datos de la BD
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Credenciales no válidas'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def userLogout(request):
    request.user.auth_token.delete() # Borrar token de usuario
    logout(request) # Cerrar sesión del usuario que hizo request
    return Response({'status': 'Se ha cerrado sesión exitosamente'},
                    status=status.HTTP_200_OK)



