from ..models.location import Location
from typing import Optional

def update_location(
    location_id,
    *,
    address: str,
    zone: str,
    latitude: int,
    longitude: int,
    description: Optional[str] = None,
    location_number: int
) -> Location:
    location = Location.objects.get(pk=location_id)
    
    location.address = address
    location.zone = zone
    location.latitude = latitude
    location.longitude = longitude
    location.description = description
    location.location_number = location_number

    location.save()
    return location