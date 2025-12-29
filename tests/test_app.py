import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Replace with a valid activity name and email for your app
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code in (200, 400, 409)  # 200: success, 400/409: already registered or invalid
    # Optionally, check response.json() for expected keys
