import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

class WeatherPredictor:
    """
    Machine Learning model to predict temperature trends
    """
    
    def __init__(self):
        """
        Initialize the ML model
        """
        self.model = LinearRegression()
    
    def predict_temperature(self, forecast_data):
        """
        Predicts temperature trend using Linear Regression
        
        Parameters:
        - forecast_data: List of dictionaries with date and temp
        
        Returns:
        - Dictionary with predictions and trend analysis
        """
        try:
            # Extract temperatures from forecast
            temperatures = [day['temp'] for day in forecast_data]
            
            # Create day numbers (1, 2, 3, 4, 5, 6, 7)
            days = np.array(range(1, len(temperatures) + 1)).reshape(-1, 1)
            temps = np.array(temperatures)
            
            # Train the model
            self.model.fit(days, temps)
            
            # Predict next 3 days after the forecast
            future_days = np.array(range(len(temperatures) + 1, len(temperatures) + 4)).reshape(-1, 1)
            future_temps = self.model.predict(future_days)
            
            # Calculate trend
            slope = self.model.coef_[0]
            
            # Determine trend direction
            if slope > 0.5:
                trend = "rising"
                trend_message = "Temperatures are expected to rise in the coming days."
            elif slope < -0.5:
                trend = "falling"
                trend_message = "Temperatures are expected to fall in the coming days."
            else:
                trend = "stable"
                trend_message = "Temperatures are expected to remain stable."
            
            # Calculate average temperature
            avg_temp = round(np.mean(temperatures), 1)
            
            # Calculate temperature range
            temp_range = {
                'min': round(np.min(temperatures), 1),
                'max': round(np.max(temperatures), 1)
            }
            
            # Prepare predictions
            predictions = {
                'trend': trend,
                'trend_message': trend_message,
                'avg_temp': avg_temp,
                'temp_range': temp_range,
                'slope': round(slope, 2),
                'future_predictions': [
                    {
                        'day': f'Day {i+1}',
                        'temp': round(temp, 1)
                    }
                    for i, temp in enumerate(future_temps)
                ]
            }
            
            return predictions
        
        except Exception as e:
            # Return default values if prediction fails
            return {
                'trend': 'unknown',
                'trend_message': 'Unable to generate predictions.',
                'avg_temp': 0,
                'temp_range': {'min': 0, 'max': 0},
                'slope': 0,
                'future_predictions': []
            }