from pydantic import BaseModel
from typing import List

class WeatherCondition(BaseModel):
    main: str
    description: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
