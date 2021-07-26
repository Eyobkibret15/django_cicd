import json

import pytest
from django.urls import reverse
from .models import *
from .views import *

pytestmark = pytest.mark.django_db
studenturl ="http://127.0.0.1:8000/student/"


def test_views(client):
    obj = client.get(studenturl)
    assert obj.status_code == 200

def test_post(client):
    obj = client.post(studenturl ,data={"name":"eyoba","grade":"2"})
    assert obj.status_code == 201

def test_false_post(client):
    obj = client.post(studenturl, data={"name": "eyobdfa", "grade": "2"})
    assert obj.status_code == 400

def test_specific_get(client):
    test_data =student.objects.create(name="miko",grade="24.00")
    obj = client.post(studenturl ,{"name": "eyoba",
        "grade": "12"})
    data =json.loads(obj.content)
    assert obj.status_code == 201
