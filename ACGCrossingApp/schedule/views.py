from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Location, Shift
from .serializers import LocationSerializer, ShiftSerializer, ShiftWriteSerializer
from rest_framework import authentication, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view


@csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def locations(request):
    """
    List all locations
    """
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def shifts(request):
    """
    List all shifts, or create a new one
    """
    if request.method == 'GET':
        shifts = Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ShiftWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


