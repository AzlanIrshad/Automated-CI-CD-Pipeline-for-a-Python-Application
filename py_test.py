# test_contact_app_pytest.py

import pytest
from app import app

@pytest.fixture
def client():
    """Setup for the Flask app test client"""
    with app.test_client() as client:
        app.testing = True
        yield client

def test_homepage(client):
    """Test the homepage route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Contacts' in response.data

def test_add_contact(client):
    """Test adding a new contact"""
    response = client.post('/new', data={'name': 'Jane Doe', 'phone': '9876543210'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Jane Doe' in response.data
    assert b'9876543210' in response.data
