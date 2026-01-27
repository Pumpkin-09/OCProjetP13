import pytest
from lettings.models import Letting, Address


@pytest.fixture
def letting_adresse_titre():
    address = Address.objects.create(
        number=123,
        street="street test",
        city="city test",
        state="ST",
        zip_code=456,
        country_iso_code="FRA"
        )

    letting = Letting.objects.create(
        title="test titre",
        address=address
        )
    return letting
