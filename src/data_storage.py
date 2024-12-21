import json
import random


def load_data(filename):
    """
    Load data from a JSON file. If the file does not exist, return an empty dictionary.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data, filename):
    """
    Save data to a JSON file.
    """
    pass


def get_random_exercise(data):
    workout = {}
    for category, groups in data.items():
        workout[category] = {}
        if isinstance(groups, dict):
            # If there are subcategories
            for group, exercises in groups.items():
                workout[category][group] = random.choice(exercises)
        else:  # If there are no subcategories
            workout[category] = random.choice(groups)
    return workout
