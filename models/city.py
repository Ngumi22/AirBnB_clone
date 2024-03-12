#!/usr/bin/python3
"""Defines city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents the city

    attributes:
    state_id(str): The state id.
    name(state): Name of the city
    """
    state_id = ""
    name = ""
