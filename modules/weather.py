import requests

def get_weather_forecast(city: str) -> str:
    api_key = "df925a02fde9f8ad1a26ffd776acf4ed"  # Replace with your real OpenWeatherMap API key
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()

        if res.get("main"):
            temp = res["main"]["temp"]
            weather = res["weather"][0]["description"]
            humidity = res["main"]["humidity"]
            return f"{city.title()} - {temp}°C, {weather}, Humidity: {humidity}%"
        else:
            return "City not found or weather data unavailable."
    except Exception as e:
        return f"Weather fetch failed: {str(e)}"
