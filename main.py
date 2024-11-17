from fastapi import FastAPI, HTTPException
from services.weather_service import fetch_city_coordinates, fetch_weather_by_coords
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        # Fetch coordinates for the city
        lat, lon = await fetch_city_coordinates(city)
        
        # Fetch the weather using the coordinates
        weather = await fetch_weather_by_coords(lat, lon)
        
        return weather
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching weather data.")
