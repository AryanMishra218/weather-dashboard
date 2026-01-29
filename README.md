# 🌤️ Weather Dashboard - Real-time Weather with AI Predictions

A professional weather application that provides real-time weather data and uses Machine Learning to predict temperature trends.

## ✨ Features

- **Real-time Weather Data**: Get current weather for any city worldwide
- **7-Day Forecast**: View detailed weather forecast for the next week
- **AI-Powered Predictions**: Machine Learning model predicts temperature trends
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Weather Details**: Temperature, humidity, wind speed, pressure, and more

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn (Linear Regression)
- **API**: OpenWeatherMap API
- **Data Processing**: Pandas, NumPy

## 📁 Project Structure
```
weather-dashboard/
├── templates/
│   └── index.html          # Main HTML page
├── static/
│   ├── css/
│   │   └── style.css       # Styling
│   └── js/
│       └── script.js       # Frontend logic
├── app.py                  # Flask backend server
├── weather_ml.py           # ML prediction model
├── requirements.txt        # Python dependencies
├── .env                    # API key (not pushed to GitHub)
└── README.md              # Project documentation
```

## 🚀 How to Run

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file and add your OpenWeatherMap API key
4. Run the app: `python app.py`
5. Open browser: `http://localhost:5000`

## 🤖 How the ML Works

The application uses **Linear Regression** to analyze temperature patterns:
- Takes 7-day forecast data as input
- Learns the temperature trend (rising/falling/stable)
- Predicts next 3 days of temperatures
- Calculates average temperature and range

## 📸 Features Overview

- Search any city worldwide
- View current temperature and weather conditions
- See "feels like" temperature, humidity, wind speed
- AI analyzes temperature trends
- 7-day forecast with weather icons
- Fully responsive design

## 🔑 API Key Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Create `.env` file in project root
4. Add: `WEATHER_API_KEY=your_api_key_here`

## 👨‍💻 Author
**Aryan Mishra**
- GitHub: [@AryanMishra218](https://github.com/AryanMishra218)
Built as a learning project to demonstrate:
- Full-stack web development
- API integration
- Machine Learning implementation
- Professional coding practices

## 📝 License

This project is open source and available for learning purposes.
