#!/usr/bin/python3
"""creates an object from json file"""


import json


def load_from_json_file(filename):
    """h"""
    with open(filename, "r") as f:
        return json.load(f)
