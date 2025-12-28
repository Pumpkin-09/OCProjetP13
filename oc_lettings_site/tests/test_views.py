from unittest.mock import patch
import pytest

from django.urls import reverse, resolve
from django.test import Client
from oc_lettings_site import settings, views
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_views_url_200():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()

    assert resolve(path).func == views.index
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
    assert reverse('profiles_index') in content
    assert reverse('lettings_index') in content


@pytest.mark.django_db
def test_index_views_url_404():
    client = Client()
    path = '/error_404'  # assuming 'error_404' is not a defined route
    response = client.get(path)

    assert response.status_code == 404
    assertTemplateUsed(response, '404.html')

