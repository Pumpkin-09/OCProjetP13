from django.urls import reverse, resolve
from oc_lettings_site import views


def test_home_url():
    path = reverse('index')
    assert resolve(path).func == views.index
