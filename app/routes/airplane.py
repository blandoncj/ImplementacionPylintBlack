"""
Airplane routes module.

This module defines the routes for managing airplane data using FastAPI.
"""

from fastapi import APIRouter
from schemas.airplane import AirplaneSchema
from services.airplane import *

airplane_router = APIRouter()

@airplane_router.get("/")
def get_airplanes():
    """
    Retrieves a list of all airplanes.

    Returns:
        List[dict]: A list of dictionaries representing all airplanes.
    """
    return get_all_airplanes()

@airplane_router.get('/{id}')
def get_airplane(airplane_id:int):
    """
    Retrieves a specific airplane by its ID.

    Args:
        airplane_id (int): The ID of the airplane to retrieve.

    Returns:
        dict: A dictionary representing the airplane if found.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    return get_airplane_by_id(airplane_id)

@airplane_router.post('/')
def register_airplane(airplane: AirplaneSchema):
    """
    Registers a new airplane.

    Args:
        airplane (AirplaneSchema): The data of the airplane to register.

    Returns:
        dict: A dictionary with the created airplane data.
    """
    return create_airplane(airplane)

@airplane_router.put('/{id}')
def update_airplane_data(airplane_id: int, airplane: AirplaneSchema):
    """
    Updates an existing airplane's data by its ID.

    Args:
        airplane_id (int): The ID of the airplane to update.
        airplane (AirplaneSchema): The updated data of the airplane.

    Returns:
        dict: A dictionary with the update confirmation message.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    return update_airplane(airplane_id, airplane)

@airplane_router.delete('/{id}')
def remove_airplane(airplane_id: int):
    """
    Deletes an airplane by its ID.

    Args:
        airplane_id (int): The ID of the airplane to delete.

    Returns:
        dict: A dictionary with the deletion confirmation message.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    return delete_airplane(airplane_id)