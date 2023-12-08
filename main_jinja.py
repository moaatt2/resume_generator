
# Imports
import os
import json
from jinja2 import Environment, FileSystemLoader

# Settings
DATA_FILE = 'data.json'
MAX_SKILLS_LEN = 70

# Load data
with open(DATA_FILE, 'r') as json_file:
    data = json.load(json_file)

environment = Environment(loader=FileSystemLoader('templates/'))
template = environment.get_template('resume.txt')

content = template.render(
    data
)

print(content)