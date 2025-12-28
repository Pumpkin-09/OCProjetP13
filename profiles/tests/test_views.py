import pytest

from django.urls import reverse, resolve
from django.test import Client
from profiles import views
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_views_url_200(three_profiles_user):
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)

    assert resolve(path).func == views.index
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_views(three_profiles_user):
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()

    assert len(response.context['profiles_list']) == 3
    assert "testuser1" in content
    assert "testuser2" in content
    assert "testuser3" in content

    assertTemplateUsed(response, 'profiles/index.html')
    assert reverse('lettings_index') in content
    assert reverse('index') in content


@pytest.mark.django_db
def test_profile_url_200(profile_user):
    client = Client()
    path = reverse('profile', kwargs={'username': profile_user.user.username})
    response = client.get(path)

    assert resolve(path).func == views.profile
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')


@pytest.mark.django_db
def test_profile(profile_user):
    client = Client()
    path = reverse('profile', kwargs={'username': profile_user.user.username})
    response = client.get(path)
    content = response.content.decode()

    assert profile_user.user.username in content
    assert profile_user.favorite_city in content
    assert profile_user.user.first_name in content
    assert profile_user.user.last_name in content
    assert profile_user.user.email in content
