"""
Module: cookbook.py
This module contains the schema definition for a cookbook.
Classes:
- CookBookSchema: A Pydantic BaseModel representing a cookbook.
"""

from datetime import datetime
from pydantic import BaseModel, Field, validator


class CookBookSchema(BaseModel):
    """
    CookBookSchema
    This class represents the schema for a cookbook.
    Attributes:
    - title (str): The title of the cookbook.
    - author (str): The author of the cookbook.
    - publication_year (int): The publication year of the cookbook.
    - price (float): The price of the cookbook.
    - isbn (str): The ISBN of the cookbook.
    - num_pages (int): The number of pages in the cookbook.
    - description (str): The description of the cookbook.
    """

    isbn: str = Field(..., min_length=10, max_length=10)
    title: str = Field(..., min_length=1, max_length=50)
    author: str = Field(..., min_length=1, max_length=50)
    publication_year: int = Field(..., gt=0, lt=2024)
    price: float = Field(..., gt=0.0)
    num_pages: int = Field(..., gt=0)

    @validator("isbn")
    def validate_isbn(cls, isbn):
        """
        Validates the ISBN.
        Args:
            cls: The class object.
            isbn (str): The ISBN to be validated.
        Raises:
            ValueError: If the ISBN is not exactly 10 digits.
        Returns:
            str: The validated ISBN.
        """

        if len(isbn) != 10:
            raise ValueError("ISBN must be exactly 10 digits")
        return isbn

    @validator("title")
    def validate_title(cls, title):
        """
        Validates the title of a cookbook.
        Args:
            cls: The class object.
            title (str): The title to be validated.
        Raises:
            ValueError: If the title is less than 3 characters long.
        Returns:
            str: The validated title.
        """

        if len(title) < 3:
            raise ValueError("Title must be at least 3 characters long")
        return title

    @validator("author")
    def validate_author(cls, author):
        """
        Validate the author of a cookbook.
        Args:
            cls: The class object.
            author: The author to be validated.
        Raises:
            ValueError: If the author is not a string.
        Returns:
            The validated author.
        """

        if not isinstance(author, str):
            raise ValueError("Author must be a string")
        return author

    @validator("publication_year")
    def validate_publication_year(cls, publication_year):
        """
        Validates the publication year of a cookbook.
        Args:
            cls (type): The class object.
            publication_year (int): The publication year to be validated.
        Raises:
            ValueError: If the publication year is not between 1900 and the current year.
        Returns:
            int: The validated publication year.
        """

        current_year = datetime.now().year
        if publication_year < 1900 or publication_year > current_year:
            raise ValueError("Publication year must be between 1900 and current year")
        return publication_year

    @validator("price")
    def validate_price(cls, price):
        """
        Validates the price of a cookbook.
        Args:
            cls: The class object.
            price (float): The price of the cookbook.
        Raises:
            ValueError: If the price is less than or equal to 0.
        Returns:
            float: The validated price.
        """

        if price <= 0:
            raise ValueError("Price must be a positive number")
        return price

    @validator("num_pages")
    def validate_num_pages(cls, num_pages):
        """
        Validates the number of pages for a cookbook.
        Args:
            cls (type): The class object.
            num_pages (int): The number of pages to validate.
        Raises:
            ValueError: If the number of pages is not a positive integer.
        Returns:
            int: The validated number of pages.
        """

        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError("Number of pages must be a positive integer")
        return num_pages
