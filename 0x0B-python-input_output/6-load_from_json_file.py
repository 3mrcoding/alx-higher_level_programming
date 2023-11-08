#!/usr/bin/python3

"""Define a file that contain JSON string function"""
import json


def load_from_json_file(filename):

    """a function that creates an Object from a “JSON file”"""

    with open(filename) as file:
        return json.load(file)
