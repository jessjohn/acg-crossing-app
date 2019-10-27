from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Location
from .serializers import LocationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view


@csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def locations_list(request):
    """
    List all locations
    """
    snippets = Location.objects.all()
    serializer = LocationSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)
