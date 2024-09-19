"""
Cookbook service
"""

from fastapi import Body, HTTPException
from database import Cookbook
from schemas.cookbook import CookbookSchema


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
    except Cookbook.DoesNotExist:
        raise HTTPException(status_code=404, detail='Cookbook not found')

def create_cookbook(cookbook: CookbookSchema = Body(...)):
    """
    Creates a new cookbook record in the database.

    Args:
        cookbook (CookbookSchema): The schema containing cookbook data.

    Returns:
        Cookbook: The newly created cookbook record.
    """
    return Cookbook.create(**cookbook.dict())

def update_cookbook(cookbook_id: int, cookbook: CookbookSchema = Body(...)):
    """
    Updates an existing cookbook record by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to update.
        cookbook (CookbookSchema): The schema with updated cookbook data.

    Returns:
        dict: A success message upon updating the cookbook.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    try:
        Cookbook.get(Cookbook.id == cookbook_id)
    except Cookbook.DoesNotExist:
        raise HTTPException(status_code=404, detail='Cookbook not found')

    Cookbook.update(**cookbook.dict()).where(Cookbook.id == cookbook_id).execute()
    return {'message': 'Cookbook updated successfully'}

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
    except Cookbook.DoesNotExist:
        raise HTTPException(status_code=404, detail='Cookbook not found')

    Cookbook.delete().where(Cookbook.id == cookbook_id).execute()
    return {'message': 'Cookbook deleted successfully'}
