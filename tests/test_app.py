import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "0.1.0"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"healthy": True}


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.content_type.startswith("text/plain")
