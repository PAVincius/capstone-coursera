import pytest
import json
from src.app import app
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json == {'status': 'healthy'}

@patch('src.app.model_trainer')
def test_predict_endpoint_structure(mock_trainer, client):
    """
    Tests that the API accepts both country-specific and global requests
    and passes data to the model.
    """
    # Mock prediction return
    mock_trainer.predict.return_value = [100.0, 200.0]
    
    # Test Global Request
    data_global = {
        "country": "global",
        "features": [{"f1": 1, "f2": 2}, {"f1": 3, "f2": 4}]
    }
    rv = client.post('/predict', json=data_global)
    assert rv.status_code == 200
    assert 'prediction' in rv.json
    
    # Test Country Specific Request
    data_country = {
        "country": "brazil",
        "features": [{"f1": 5, "f2": 6}]
    }
    rv = client.post('/predict', json=data_country)
    assert rv.status_code == 200
    # In a real app, we'd verify that the country arg was used to filter/select models
    
def test_predict_no_features(client):
    rv = client.post('/predict', json={"country": "usa"})
    assert rv.status_code == 400
