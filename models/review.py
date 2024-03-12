#!/usr/bin/python3
"""Defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review class

    attributes:
    place_id (str): Id of the place reviewed
    user_id (str): Id of the user writing the review
    text (str): The review body
    """
    place_id = ""
    user_id = ""
    text = ""
