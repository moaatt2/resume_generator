
# Imports
import os
import json
from typing import List
from jinja2 import Environment, FileSystemLoader

# Settings
DATA_FILE = 'data.json'
MAX_SKILLS_LEN = 70

# Load data
with open(DATA_FILE, 'r') as json_file:
    data = json.load(json_file)


# Write a helper function to format skills into lines
def create_skill_lines(skills: List[str]) -> List[str]:
    out = list()
    line = ''

    for item in skills:
        if len(line) + len(item) + 2 <= MAX_SKILLS_LEN:
            line = line + item + ', '
        else:
            out.append(line)
            line = item + ', '
    out.append(line)
    return out


# Format Technical Skill Lines
stack_lines = create_skill_lines(data['technical_skills']['solution_stack'])
software_lines = create_skill_lines(data['technical_skills']['software_tools'])

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

# Remove logfile
os.remove('output\\compiled_results\\resume.log')
