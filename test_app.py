import pytest
from app import app

def test_time_route():
    client = app.test_client()
    response = client.get('/time')
    data = response.get_json()
    assert data['time'] > 0

def test_metrics_route():
    client = app.test_client()
    initial_res = client.get('/metrics')
    initial_count = initial_res.get_json().get('count', 0)
    client.get('/time')
    response = client.get('/metrics')
    data = response.get_json()
    assert data['count'] == initial_count + 1
