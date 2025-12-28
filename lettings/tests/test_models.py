import pytest


@pytest.mark.django_db
def test_letting_str(letting_adresse_titre):
    address = letting_adresse_titre.address
    letting = letting_adresse_titre

    assert str(letting) == "test titre"
    assert str(address) == "123 street test"


@pytest.mark.django_db
def test_letting_address(letting_adresse_titre):
    address = letting_adresse_titre.address
    
    assert address.number == 123
    assert address.street == "street test"
    assert address.city == "city test"
    assert address.state == "ST"
    assert address.zip_code == 456
    assert address.country_iso_code == "FRA"