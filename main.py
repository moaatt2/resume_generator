
# Imports
import os
import json
from typing import List
from jinja2 import Environment, FileSystemLoader

# Settings
DATA_FILE = 'data_versions.json'
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


# Handle Implicit Single Version Case
if 'versions' not in data:
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

# Handle Case Where Versions are Defined
else:
    for version in data.get("versions", list()):
        vdata = dict()

        # Set Nam
        vdata['name'] = data['name']

        # Get Contact Info
        contact_info = list()
        for i in data['contact_info']:
            if version in i['versions']:
                contact_info.append(i['data'])
        vdata['contact_info'] = contact_info

        # Get Professional Overview Points
        prof_overview = list()
        for i in data['professional_overview']:
            if version in i['versions']:
                prof_overview.append(i['data'])
        vdata['professional_overview'] = prof_overview

        # Format Solution Stack Lines
        stack_items = list()
        for i in data['technical_skills']['solution_stack']:
            if version in i['versions']:
                stack_items.append(i['data'])
        stack_lines = create_skill_lines(stack_items)

        # Format Software Tools Lines
        software_items = list()
        for i in data['technical_skills']['software_tools']:
            if version in i['versions']:
                software_items.append(i['data'])
        software_lines = create_skill_lines(software_items)

        # Handle Education
        vdata["education"] = list()
        for i in data["education"]:
            if version in i['versions']:
                points = list()
                for p in i['points']:
                    if version in p['versions']:
                        points.append(p['data'])
                vdata["education"].append({
                    "institution": i["institution"],
                    "location":    i["location"],
                    "degree":      i["degree"],
                    "time":        i["time"],
                    "points":      points,
                })

        # Handle Experience
        vdata["experience"] = list()
        for i in data["experience"]:
            if version in i['versions']:
                points = list()
                for p in i['points']:
                    if version in p['versions']:
                        points.append(p['data'])
                vdata["experience"].append({
                    "company":  i["company"],
                    "location": i["location"],
                    "title":    i["title"],
                    "time":        i["time"],
                    "points":      points,
                })

        # Fill out jinja template
        environment = Environment(loader=FileSystemLoader('templates/'), trim_blocks=True, lstrip_blocks=True)
        template = environment.get_template('resume.txt')
        content = template.render(
            vdata,
            stack_lines=stack_lines,
            software_lines=software_lines,
        )

