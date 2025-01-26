import requests
from datetime import datetime, timedelta

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_forecast(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch weather data")
        return None

def main():
    city_name = "Kutaisi"  # Replace with the city name you want to fetch data for
    api_key = "d837c474751e98fb8d504d44d00494a9"  # Replace with your OpenWeatherMap API key
    forecast_data = get_weather_forecast(city_name, api_key)
    if forecast_data:
        print("3-Day Weather Forecast for", city_name)
        today = datetime.utcnow()
        end_date = today + timedelta(days=3)
        for forecast in forecast_data['list']:
            date_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if date_time < end_date:
                weather_description = forecast['weather'][0]['description']
                temperature = kelvin_to_celsius(forecast['main']['temp'])
                print(f"Date & Time: {date_time}, Weather: {weather_description}, Temperature: {temperature:.2f}°C")

if __name__ == "__main__":
    main()
