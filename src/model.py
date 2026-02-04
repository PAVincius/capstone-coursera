import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from .logger import get_logger

logger = get_logger("MODEL")

class ModelTrainer:
    def __init__(self):
        self.model = None

    def train(self, df, target_column, model_type="random_forest"):
        logger.info(f"Training model: {model_type}")
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        if model_type == "random_forest":
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == "linear_regression":
            self.model = LinearRegression()
        else:
            raise ValueError("Unsupported model type")
            
        self.model.fit(X_train, y_train)
        
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        logger.info(f"Model trained. MSE: {mse}")
        return mse

    def save_model(self, file_path):
        if self.model:
            joblib.dump(self.model, file_path)
            logger.info(f"Model saved to {file_path}")
        else:
            logger.warning("No model to save.")

    def load_model(self, file_path):
        if os.path.exists(file_path):
            self.model = joblib.load(file_path)
            logger.info(f"Model loaded from {file_path}")
        else:
            logger.error(f"Model file not found: {file_path}")

    def predict(self, input_data):
        if self.model:
            return self.model.predict(input_data)
        else:
            raise Exception("Model not loaded/trained")
