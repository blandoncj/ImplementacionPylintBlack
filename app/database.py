"""
Database module for the API.
"""

import os
from peewee import (
    Model,
    MySQLDatabase,
    AutoField,
    CharField,
    IntegerField,
    FloatField,
)
from dotenv import load_dotenv

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class Airplane(Model):
    """
    Represents an airplane entity in the database.

    Attributes:
        id (AutoField): The primary key for the airplane.
        model (CharField): The model name of the airplane (max 50 characters).
        manufacture_year (IntegerField): The year the airplane was manufactured.
        seats (IntegerField): The number of seats in the airplane.
        airline (CharField): The name of the airline operating the airplane (max 50 characters).
        max_speed (FloatField): The maximum speed of the airplane.
        weight (FloatField): The weight of the airplane.
    """

    id = AutoField()
    model = CharField(max_length=50)
    manufacture_year = IntegerField()
    seats = IntegerField()
    airline = CharField(max_length=50)
    max_speed = FloatField()
    weight = FloatField()

    class Meta:
        """
        Meta class for specifying the database and table name.

        Attributes:
            database (MySQLDatabase): The database connection used by the model.
            table_name (str): The name of the table in the database.
        """

        # pylint: disable=too-few-public-methods
        database = database
        table_name = "airplanes"
