import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"CloudDeploy" in response.data


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_status_endpoint():
    client = app.test_client()

    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json["status"] == "operational"


def test_version_endpoint():
    client = app.test_client()

    response = client.get("/api/version")

    assert response.status_code == 200