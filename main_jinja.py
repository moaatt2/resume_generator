
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


# Format Solution Stack
stack_lines = list()
line = ''
for i in data['technical_skills']['solution_stack']:
    if len(line) + len(i) + 2 <= MAX_SKILLS_LEN:
        line = line + i + ', '
    else:
        stack_lines.append(line)
        line = i + ', '
stack_lines.append(line)


# Format Software/Tools
software_lines = list()
line = ''
for i in data['technical_skills']['software_tools']:
    if len(line) + len(i) + 2 <= MAX_SKILLS_LEN:
        line = line + i + ', '
    else:
        software_lines.append(line)
        line = i + ', '
software_lines.append(line)


# Fill out jinja template
environment = Environment(loader=FileSystemLoader('templates/'), trim_blocks=True, lstrip_blocks=True)
template = environment.get_template('resume.txt')
content = template.render(
    data,
    stack_lines=stack_lines,
    software_lines=software_lines,
)

# Write output to file
with open('output/raw_tex/resume.tex', 'w') as outfile:
    outfile.write(content)

# Compile latex file into appropriate folder
os.system("pdflatex -output-directory output\\compiled_results output\\raw_tex\\resume.tex")