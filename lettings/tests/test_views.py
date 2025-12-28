import pytest

from django.urls import reverse, resolve
from django.test import Client
from lettings import views
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_views_letting_index_url_200():
    client = Client()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()

    assert resolve(path).func == views.index
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')
    assert reverse('profiles_index') in content
    assert reverse('index') in content


@pytest.mark.django_db
def test_views_letting_url_200(letting_adresse_titre):
    client = Client()

    path = reverse('letting', kwargs={'letting_id': letting_adresse_titre.id})
    response = client.get(path)
    content = response.content.decode()

    assert resolve(path).func == views.letting
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')


@pytest.mark.django_db
def test_views_letting_url_affichage_info(letting_adresse_titre):
    client = Client()

    path = reverse('letting', kwargs={'letting_id': letting_adresse_titre.id})
    response = client.get(path)
    content = response.content.decode()

    assert ("test titre") in content
    assert ("123") in content
    assert ("street test") in content
    assert ("city test") in content
    assert ("ST") in content
    assert ("456") in content
    assert ("FRA") in content


@pytest.mark.django_db
def test_views_letting_url_lien_ok(letting_adresse_titre):
    client = Client()

    path = reverse('letting', kwargs={'letting_id': letting_adresse_titre.id})
    response = client.get(path)
    content = response.content.decode()

    assert reverse ("profiles_index") in content
    assert reverse ("index") in content
    assert reverse ("lettings_index") in content
