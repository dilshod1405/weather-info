import httpx
from config import OPENWEATHER_API_KEY, API_KEY, OPENWEATHER_API_URL

async def fetch_city_coordinates(city: str):
    """Fetch coordinates for the given city from OpenWeather's Geocoding API."""
    url = f"{OPENWEATHER_API_KEY}direct"
    params = {
        "q": city,
        "limit": 1,  # You can adjust the limit if needed
        "appid": API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    if data:
        # Extract latitude and longitude from the first result
        city_info = data[0]
        lat = city_info["lat"]
        lon = city_info["lon"]
        return lat, lon
    else:
        raise ValueError(f"City '{city}' not found.")


async def fetch_weather_by_coords(lat: float, lon: float):
    """Fetch weather data for a location given its latitude and longitude."""
    url = f"{OPENWEATHER_API_URL}weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",  # You can change to 'imperial' for Fahrenheit
        
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
