"""
Cookbook service
"""

from database import Cookbook
from schemas.cookbook import CookBookSchema
from fastapi import Body, HTTPException


def get_all_cookbooks():
    """
    Fetches all cookbook records from the database.

    Returns:
        List[dict]: A list of dictionaries representing all cookbooks.
    """
    return list(Cookbook.select().dicts())


def get_cookbook_by_id(cookbook_id: int):
    """
    Fetches a specific cookbook by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to retrieve.

    Returns:
        Cookbook: The cookbook record if found.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    try:
        return Cookbook.get(Cookbook.id == cookbook_id)
    except Cookbook.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Cookbook not found") from exc


def create_cookbook(cookbook: CookBookSchema = Body(...)):
    """
    Creates a new cookbook record in the database.

    Args:
        cookbook (CookBookSchema): The schema containing cookbook data.

    Returns:
        Cookbook: The newly created cookbook record.
    """
    return Cookbook.create(**cookbook.dict())


def update_cookbook(cookbook_id: int, cookbook: CookBookSchema = Body(...)):
    """
    Updates an existing cookbook record by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to update.
        cookbook (CookBookSchema): The schema with updated cookbook data.

    Returns:
        dict: A success message upon updating the cookbook.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    try:
        Cookbook.get(Cookbook.id == cookbook_id)
    except Cookbook.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Cookbook not found") from exc

    Cookbook.update(**cookbook.dict()).where(Cookbook.id == cookbook_id).execute()
    return {"message": "Cookbook updated successfully"}


def delete_cookbook(cookbook_id: int):
    """
    Deletes a cookbook record by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to delete.

    Returns:
        dict: A success message upon deleting the cookbook.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    try:
        Cookbook.get(Cookbook.id == cookbook_id)
    except Cookbook.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Cookbook not found") from exc

    Cookbook.delete().where(Cookbook.id == cookbook_id).execute()
    return {"message": "Cookbook deleted successfully"}
