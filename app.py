from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from weather_ml import WeatherPredictor

# Load environment variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5'

# Initialize ML predictor
predictor = WeatherPredictor()

@app.route('/')
def home():
    """
    Serves the main HTML page
    """
    return render_template('/index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    """
    Gets current weather and forecast for a city
    """
    try:
        # Get city name from user request
        data = request.get_json()
        city = data.get('city', '')
        
        if not city:
            return jsonify({'error': 'Please enter a city name'}), 400
        
        # Get current weather
        current_url = f'{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric'
        current_response = requests.get(current_url)
        
        if current_response.status_code != 200:
            return jsonify({'error': 'City not found. Please check the spelling.'}), 404
        
        current_data = current_response.json()
        
        # Get 7-day forecast
        lat = current_data['coord']['lat']
        lon = current_data['coord']['lon']
        forecast_url = f'{BASE_URL}/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()
        
        # Process forecast data (get one reading per day)
        daily_forecast = []
        seen_dates = set()
        
        for item in forecast_data['list']:
            date = item['dt_txt'].split(' ')[0]
            if date not in seen_dates and len(daily_forecast) < 7:
                daily_forecast.append({
                    'date': date,
                    'temp': round(item['main']['temp'], 1),
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon']
                })
                seen_dates.add(date)
        
        # Get ML predictions
        predictions = predictor.predict_temperature(daily_forecast)
        
        # Prepare response
        weather_info = {
            'city': current_data['name'],
            'country': current_data['sys']['country'],
            'current': {
                'temp': round(current_data['main']['temp'], 1),
                'feels_like': round(current_data['main']['feels_like'], 1),
                'humidity': current_data['main']['humidity'],
                'pressure': current_data['main']['pressure'],
                'wind_speed': round(current_data['wind']['speed'], 1),
                'description': current_data['weather'][0]['description'],
                'icon': current_data['weather'][0]['icon']
            },
            'forecast': daily_forecast,
            'predictions': predictions
        }
        
        return jsonify(weather_info)
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)