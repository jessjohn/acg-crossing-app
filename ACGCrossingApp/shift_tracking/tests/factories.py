import factory

from ..models.location import Location

class LocationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'shift_tracking.Location'
        django_get_or_create = (
            'address',
            'zone',
            'latitude',
            'longitude',
            'description',
            'location_number',
        )

    address = factory.Faker('address')
    zone = factory.Faker('city')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    description = factory.Faker('sentence')
    location_number = factory.Faker('random_number')