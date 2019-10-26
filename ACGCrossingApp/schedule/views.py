from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Location
from .serializers import LocationSerializer


@csrf_exempt
def locations_list(request):
    """
    List all locations
    """
    if request.method == 'GET':
        snippets = Location.objects.all()
        serializer = LocationSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
