from django.urls import reverse, resolve
from lettings import views


def test_lettings_index_url():
    path = reverse('lettings_index')
    assert resolve(path).func == views.index


def test_lettings_letting_url():
    path = reverse('letting', kwargs={'letting_id': 1})
    assert resolve(path).func == views.letting
