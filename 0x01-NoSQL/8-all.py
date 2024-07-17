#!/usr/bin/env/python3
"""  python function that lists all documents in python """
def list_all(mongo_collection):
    """
    it lists all documents in a collection
    """
    return list(mongo_collection.find())
