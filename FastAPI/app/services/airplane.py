"""
Airplane service
"""

from database import Airplane
from schemas.airplane import AirplaneSchema
from fastapi import Body, HTTPException


def get_all_airplanes():
    """
    Fetches all airplane records from the database.

    Returns:
        List[dict]: A list of dictionaries representing all airplanes.
    """
    return list(Airplane.select().dicts())


def get_airplane_by_id(airplane_id: int):
    """
    Fetches a specific airplane by its ID.

    Args:
        airplane_id (int): The ID of the airplane to retrieve.

    Returns:
        Airplane: The airplane record if found.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    try:
        return Airplane.get(Airplane.id == airplane_id)
    except Airplane.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Airplane not found") from exc


def create_airplane(airplane: AirplaneSchema = Body(...)):
    """
    Creates a new airplane record in the database.

    Args:
        airplane (AirplaneSchema): The schema containing airplane data.

    Returns:
        Airplane: The newly created airplane record.
    """
    return Airplane.create(**airplane.dict())


def update_airplane(airplane_id: int, airplane: AirplaneSchema = Body(...)):
    """
    Updates an existing airplane record by its ID.

    Args:
        airplane_id (int): The ID of the airplane to update.
        airplane (AirplaneSchema): The schema with updated airplane data.

    Returns:
        dict: A success message upon updating the airplane.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    try:
        Airplane.get(Airplane.id == airplane_id)
    except Airplane.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Airplane not found") from exc

    Airplane.update(**airplane.dict()).where(Airplane.id == airplane_id).execute()
    return {"message": "Airplane updated successfully"}


def delete_airplane(airplane_id: int):
    """
    Deletes an airplane record by its ID.

    Args:
        airplane_id (int): The ID of the airplane to delete.

    Returns:
        dict: A success message upon deleting the airplane.

    Raises:
        HTTPException: If no airplane with the given ID is found (404).
    """
    try:
        Airplane.get(Airplane.id == airplane_id)
    except Airplane.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Airplane not found") from exc

    Airplane.delete().where(Airplane.id == airplane_id).execute()
    return {"message": "Airplane deleted successfully"}
