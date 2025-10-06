import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_config():
    """
    Fixture to create a mock configuration object.
    """
    mock_cfg = MagicMock()
    mock_cfg.hostname = "test-service"
    mock_cfg.ext_srv.redis_srv.host = "localhost"
    mock_cfg.ext_srv.redis_srv.port = 6379
    mock_cfg.ext_srv.redis_srv.db = 0
    return mock_cfg

@pytest.fixture
def client(mock_config):
    """
    Test client fixture that mocks the configuration loading
    before the app is imported and the client is created.
    """
    with patch('rv16_lib.get_object_from_config', return_value=mock_config):
        with patch('service.get_object_from_config', return_value=mock_config):
            with patch('app.app.srv') as mock_service:
                mock_service.initialize_service()

                from app.app import app
                yield TestClient(app)


def test_health_check_get(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_check_post(client):
    request_data = {"key": "value"}
    response = client.post("/health", json=request_data)
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": request_data}


def test_register_service(client):
    request_data = {
        "provider": "local",
        "service": "test_service",
        "configuration": {"param": "value"}
    }

    with patch('app.api.routers.endpoints.srv') as mock_srv:
        mock_srv.initalize_service()

        response = client.post("/register-service", json=request_data)

        assert response.status_code == 200
        assert response.json() == {"result": "success"}
        mock_srv.get_provider.assert_called_once_with("LOCAL")
        mock_provider.register_service.assert_called_once_with(
            service="test_service",
            configuration={"param": "value"}
        )