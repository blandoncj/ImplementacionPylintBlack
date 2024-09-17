""" 
Airplane schema module.
"""

from datetime import datetime
from pydantic import BaseModel, Field, validator


class AirplaneSchema(BaseModel):
    """
    Represents an airplane with model, year, seats, airline, speed, and weight.
    """

    model: str = Field(..., max_length=50)
    manufacture_year: int = Field(..., gt=1900, lt=2024)
    seats: int = Field(..., gt=0)
    airline: str = Field(..., max_length=50)
    max_speed: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)

    class Config:
        """Strips leading/trailing whitespace."""

        # pylint: disable=too-few-public-methods
        anystr_strip_whitespace = True

    @validator("model")
    def validate_model_length(cls, model):
        """
        Validates that the model name has at least 3 characters.

        Args:
            model (str): The model name of the airplane.

        Returns:
            str: The validated model name.

        Raises:
            ValueError: If the model name is less than 3 characters.
        """
        if len(model) < 3:
            raise ValueError("Model name must have at least 3 characters")
        return model

    @validator("manufacture_year")
    def validate_manufacture_year(cls, year):
        """
        Validates that the manufacture year is not in the future.

        Args:
            year (int): The manufacture year of the airplane.

        Returns:
            int: The validated manufacture year.

        Raises:
            ValueError: If the manufacture year is in the future.
        """
        current_year = datetime.now().year
        if year > current_year:
            raise ValueError("Manufacture year cannot be in the future")
        return year

    @validator("seats")
    def validate_seats(cls, seats):
        """
        Validates that the number of seats is a positive even number.

        Args:
            seats (int): The number of seats in the airplane.

        Returns:
            int: The validated number of seats.

        Raises:
            ValueError: If the number of seats is not an even number.
        """
        if seats % 2 != 0:
            raise ValueError("Number of seats must be an even number")
        return seats

    @validator("airline")
    def validate_airline_length(cls, airline):
        """
        Validates that the airline name has at least 5 characters.

        Args:
            airline (str): The name of the airline.

        Returns:
            str: The validated airline name.

        Raises:
            ValueError: If the airline name is less than 5 characters.
        """
        if len(airline) < 5:
            raise ValueError("Airline name must have at least 5 characters")
        return airline
