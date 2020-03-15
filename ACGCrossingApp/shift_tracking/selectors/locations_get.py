from django.db.models import Q
from ..models.location import Location
from typing import Optional, Iterable

# Just get all of the locations
def get_locations() -> Iterable[Location]:
    return Location.objects.all()

# Just get the location by id specified
def get_location(
    *,
    id: int
) -> Location:
    query = Q(pk=id)
    return Location.objects.get(query)