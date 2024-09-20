"""
Cookbook routes module.

This module defines the routes for managing cookbook data using FastAPI.
"""

from schemas.cookbook import CookBookSchema

from services.cookbook import (
    get_all_cookbooks,
    get_cookbook_by_id,
    create_cookbook,
    update_cookbook,
    delete_cookbook,
)

from fastapi import APIRouter

cookbook_router = APIRouter()


@cookbook_router.get("/")
def get_cookbooks():
    """
    Retrieves a list of all cookbooks.

    Returns:
        List[dict]: A list of dictionaries representing all cookbooks.
    """
    return get_all_cookbooks()


@cookbook_router.get("/{id}")
def get_cookbook(cookbook_id: int):
    """
    Retrieves a specific cookbook by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to retrieve.

    Returns:
        dict: A dictionary representing the cookbook if found.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    return get_cookbook_by_id(cookbook_id)


@cookbook_router.post("/")
def register_cookbook(cookbook: CookBookSchema):
    """
    Registers a new cookbook.

    Args:
        cookbook (CookBookSchema): The data of the cookbook to register.

    Returns:
        dict: A dictionary with the created cookbook data.
    """
    return create_cookbook(cookbook)


@cookbook_router.put("/{id}")
def update_cookbook_data(cookbook_id: int, cookbook: CookBookSchema):
    """
    Updates an existing cookbook's data by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to update.
        cookbook (CookBookSchema): The updated data of the cookbook.

    Returns:
        dict: A dictionary with the update confirmation message.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    return update_cookbook(cookbook_id, cookbook)


@cookbook_router.delete("/{id}")
def remove_cookbook(cookbook_id: int):
    """
    Deletes a cookbook by its ID.

    Args:
        cookbook_id (int): The ID of the cookbook to delete.

    Returns:
        dict: A dictionary with the deletion confirmation message.

    Raises:
        HTTPException: If no cookbook with the given ID is found (404).
    """
    return delete_cookbook(cookbook_id)
