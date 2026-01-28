// Get weather data when user clicks button
async function getWeather() {
    const cityInput = document.getElementById('cityInput');
    const city = cityInput.value.trim();
    
    // Check if city name is entered
    if (!city) {
        showError('Please enter a city name');
        return;
    }
    
    // Hide previous results and errors
    hideError();
    hideWeather();
    showLoading();
    
    try {
        // Send request to Flask backend
        const response = await fetch('/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city: city })
        });
        
        const data = await response.json();
        
        // Check if there was an error
        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch weather data');
        }
        
        // Display the weather data
        displayWeather(data);
        
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading();
    }
}

// Display weather data on the page
function displayWeather(data) {
    // Update city name
    document.getElementById('cityName').textContent = `${data.city}, ${data.country}`;
    
    // Update current weather
    document.getElementById('mainTemp').textContent = `${data.current.temp}°C`;
    document.getElementById('weatherDesc').textContent = data.current.description;
    document.getElementById('feelsLike').textContent = `${data.current.feels_like}°C`;
    document.getElementById('humidity').textContent = `${data.current.humidity}%`;
    document.getElementById('windSpeed').textContent = `${data.current.wind_speed} m/s`;
    document.getElementById('pressure').textContent = `${data.current.pressure} hPa`;
    
    // Update weather icon
    const iconUrl = `http://openweathermap.org/img/wn/${data.current.icon}@4x.png`;
    document.getElementById('weatherIcon').src = iconUrl;
    
    // Update AI predictions
    displayPredictions(data.predictions);
    
    // Update 7-day forecast
    displayForecast(data.forecast);
    
    // Show weather display
    showWeather();
}

// Display AI predictions
function displayPredictions(predictions) {
    // Update trend
    const trendIcon = document.getElementById('trendIcon');
    const trendText = document.getElementById('trendText');
    
    if (predictions.trend === 'rising') {
        trendIcon.textContent = '📈';
        trendText.textContent = 'Temperature Rising';
    } else if (predictions.trend === 'falling') {
        trendIcon.textContent = '📉';
        trendText.textContent = 'Temperature Falling';
    } else {
        trendIcon.textContent = '➡️';
        trendText.textContent = 'Temperature Stable';
    }
    
    document.getElementById('trendMessage').textContent = predictions.trend_message;
    document.getElementById('avgTemp').textContent = `${predictions.avg_temp}°C`;
    document.getElementById('tempRange').textContent = 
        `${predictions.temp_range.min}°C to ${predictions.temp_range.max}°C`;
    
    // Display future predictions
    const futureContainer = document.getElementById('futurePredictions');
    futureContainer.innerHTML = '';
    
    predictions.future_predictions.forEach(pred => {
        const dayDiv = document.createElement('div');
        dayDiv.className = 'future-day';
        dayDiv.innerHTML = `
            <span class="future-day-label">${pred.day}</span>
            <span class="future-day-temp">${pred.temp}°C</span>
        `;
        futureContainer.appendChild(dayDiv);
    });
}

// Display 7-day forecast
function displayForecast(forecast) {
    const forecastContainer = document.getElementById('forecastContainer');
    forecastContainer.innerHTML = '';
    
    forecast.forEach(day => {
        const dayDiv = document.createElement('div');
        dayDiv.className = 'forecast-day';
        
        // Format date
        const date = new Date(day.date);
        const formattedDate = date.toLocaleDateString('en-US', { 
            month: 'short', 
            day: 'numeric' 
        });
        
        // Get icon URL
        const iconUrl = `http://openweathermap.org/img/wn/${day.icon}@2x.png`;
        
        dayDiv.innerHTML = `
            <div class="forecast-date">${formattedDate}</div>
            <img src="${iconUrl}" alt="Weather" class="forecast-icon">
            <div class="forecast-temp">${day.temp}°C</div>
            <div class="forecast-desc">${day.description}</div>
        `;
        
        forecastContainer.appendChild(dayDiv);
    });
}

// Show loading spinner
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
}

// Hide loading spinner
function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

// Hide error message
function hideError() {
    document.getElementById('errorMessage').classList.add('hidden');
}

// Show weather display
function showWeather() {
    document.getElementById('weatherDisplay').classList.remove('hidden');
}

// Hide weather display
function hideWeather() {
    document.getElementById('weatherDisplay').classList.add('hidden');
}

// Allow pressing Enter key to search
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        getWeather();
    }
}

// Add event listener for page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Weather Dashboard loaded successfully!');
});