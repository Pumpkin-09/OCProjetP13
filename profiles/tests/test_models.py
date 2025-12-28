import pytest


@pytest.mark.django_db
def test_profile_str(profile_user):
    profile = profile_user

    assert str(profile) == "testuser"
    assert profile.favorite_city == "Test City"
