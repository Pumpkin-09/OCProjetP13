from django.urls import reverse, resolve
from profiles import views


def test_profile_index_url():
    path = reverse('profiles_index')
    assert resolve(path).func == views.index


def test_profile_url():
    path = reverse('profile', kwargs={'username': 'testuser'})
    assert resolve(path).func == views.profile
