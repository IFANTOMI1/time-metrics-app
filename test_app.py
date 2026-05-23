import pytest
from app import app

def test_time_route():
    client = app.test_client()
    response = client.get('/time')
    data = response.get_json()
    assert data['time'] > 0
