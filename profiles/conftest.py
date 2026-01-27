import pytest
from profiles.models import Profile


@pytest.fixture
def profile_user(django_user_model):
    user = django_user_model.objects.create_user(
        username='testuser',
        first_name='Test',
        last_name='User',
        email='test@example.com'
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city='Test City'
    )
    return profile


@pytest.fixture
def three_profiles_user(django_user_model):
    user1 = django_user_model.objects.create_user(
        username='testuser1',
        first_name='Test',
        last_name='User1',
        email='test1@example.com'
    )
    user2 = django_user_model.objects.create_user(
        username='testuser2',
        first_name='Test',
        last_name='User2',
        email='test2@example.com'
    )
    user3 = django_user_model.objects.create_user(
        username='testuser3',
        first_name='Test',
        last_name='User3',
        email='test3@example.com'
    )
    profile1 = Profile.objects.create(
        user=user1,
        favorite_city='Test City 1'
    )
    profile2 = Profile.objects.create(
        user=user2,
        favorite_city='Test City 2'
    )
    profile3 = Profile.objects.create(
        user=user3,
        favorite_city='Test City 3'
    )
    return [profile1, profile2, profile3]
