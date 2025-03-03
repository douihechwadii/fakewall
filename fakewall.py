import json
import random
from datetime import datetime, timedelta

# loading the json settings file
def load_scenario(scenario_file):
    with open(scenario_file, 'r') as file:
        return json.load(file)