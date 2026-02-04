from flask import Flask, request, jsonify
import time
import functools
from .logger import get_logger
from .model import ModelTrainer
import pandas as pd
import os

app = Flask(__name__)
logger = get_logger("API")

# Initialize model (dummy load for structure, assuming model exists or is trained)
# In a real scenario, we might train on startup or load a pre-trained one
model_trainer = ModelTrainer()
MODEL_PATH = os.path.join("models", "model.joblib")
if os.path.exists(MODEL_PATH):
    model_trainer.load_model(MODEL_PATH)
else:
    logger.warning("No model found at startup.")

def monitor_performance(func):
    """
    Decorator to log response time and potentially accuracy drift.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        logger.info(f"Endpoint {func.__name__} took {duration:.4f} seconds.")
        return result
    return wrapper

@app.route('/predict', methods=['POST'])
@monitor_performance
def predict():
    try:
        data = request.get_json()
        country = data.get('country', 'global')
        logger.info(f"Received prediction request for country: {country}")
        
        # Here we would filter or process based on country if needed
        # For now, we assume the input features are in 'features'
        if 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
            
        input_df = pd.DataFrame(data['features'])
        
        prediction = model_trainer.predict(input_df)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
