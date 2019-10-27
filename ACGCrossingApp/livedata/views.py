from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import UserShift
from .serializers import UserShiftWriteSerializer, UserShiftReadSerializer
from rest_framework import authentication, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def user_shifts(request):
    """
    Get all user shifts, and create a new one if you post the right thing
    TODO: refine this so you filter only for the relevant day and only for upcoming shifts
    (we need to make this more efficient for real time)
    """
    if request.method == 'GET':
        user_shifts = UserShift.objects.all()
        serializer = UserShiftReadSerializer(user_shifts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserShiftWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def check_in(request):
    """
    - Make a post request with the user id, lat/lon and a yes or no answer
    - check the time of the request and match the user to their expected userShift
    - now that you have a list of shifts they COULD be doing, does the lat/long match any of them?
    - accept the check in at any that match, reject all others
    - is it no more than 10 minutes before? reject if not
    - update everything if conditions are met   
    """
    pass
