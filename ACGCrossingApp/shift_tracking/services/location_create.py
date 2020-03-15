from ..models.location import Location
from typing import Optional

def create_location(
    *,
    address: str,
    zone: str,
    latitude: int,
    longitude: int,
    description: Optional[str] = None,
    location_number: int
) -> Location:
    location = Location(
        address=address,
        zone=zone,
        latitude=latitude,
        longitude=longitude,
        description=description,
        location_number=location_number
    )
    location.full_clean()
    location.save()

    return location