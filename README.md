
# Weather Info Project

## Overview

This project is a weather information API built with FastAPI that allows users to get real-time weather data for any city using the OpenWeather API. The API provides key weather information such as temperature, humidity, and a brief weather description based on the city name passed in the URL.

### API Endpoint

- **GET** `/weather/{city}`
  - This endpoint returns the current weather details for the specified city.

#### Response Example:

```json
{
  "city": "London",
  "temperature": "15°C",
  "humidity": "75%",
  "description": "Clear sky"
}
```

## Setup and Installation

### Prerequisites:

1. Python 3.10+
2. Install FastAPI and Uvicorn

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project:

To run the project locally, use Uvicorn:

```bash
uvicorn main:app --reload
```

Your API will be running at `http://127.0.0.1:8000`.

### Example Request:

- **URL**: `http://127.0.0.1:8000/weather/London`
- 

### Acknowledgments:

- This project uses the OpenWeather API to fetch weather data.
