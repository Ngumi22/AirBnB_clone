#!/usr/bin/python3
"""Defines a place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a Place

    attributes:
    city_id (str): Id of the city
    user_id (str): Id of the user
    name (str): Name of the place
    description (str): Description of the place
    number_rooms (int): Number of rooms in the place
    number_bathrooms (int): Number of bathrooms in the place
    max_guest (int): Maximum number of guests in the place
    price_by_night (int): Price of the place by night
    latitude (float): The latitude of the place.
    longitude (float): The longitude of the place.
    amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
