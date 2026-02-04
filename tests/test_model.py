import os
import pandas as pd
import pytest
from src.model import ModelTrainer

@pytest.fixture
def dummy_data():
    return pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    })

def test_model_training_and_saving(dummy_data, tmp_path):
    trainer = ModelTrainer()
    metrics = trainer.train(dummy_data, target_column='target', model_type="random_forest")
    
    assert metrics >= 0
    
    save_path = tmp_path / "model.joblib"
    trainer.save_model(str(save_path))
    
    assert os.path.exists(save_path)
    
    # Test loading
    new_trainer = ModelTrainer()
    new_trainer.load_model(str(save_path))
    assert new_trainer.model is not None
