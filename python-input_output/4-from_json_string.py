#!/usr/bin/python3
"""Returns an object"""


import json


def from_json_string(my_str):
    """represented by json file"""
    return json.loads(my_str)
