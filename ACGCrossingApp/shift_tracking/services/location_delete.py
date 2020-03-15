from ..selectors.locations_get import get_location
from ..models.location import Location

def delete_location(location_id: int) -> None:
    location = get_location(id=location_id)
    location.delete()