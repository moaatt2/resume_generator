
######################################################################
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
######################################################################

# Imports
import json

# Settings
DATA_FILE = 'data.json'
MAX_SKILLS_LEN = 70

# Load data
with open(DATA_FILE, 'r') as json_file:
    data = json.load(json_file)


#
out = f"""
%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\\documentclass{{resume}}
% Use the custom resume.cls style

\\usepackage{{fontawesome5}}
\\usepackage{{amsmath}}
\\usepackage{{tabularx}}
\\usepackage{{scalerel}}

\\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{{geometry}} % Document margins
\\newcommand{{\\tab}}[1]{{\\hspace{{.2667\\textwidth}}\\rlap{{#1}}}}
\\newcommand{{\\itab}}[1]{{\\hspace{{0em}}\\rlap{{#1}}}}

\\usepackage{{color,hyperref}}
\\definecolor{{darkblue}}{{rgb}}{{0.0,0.0,0.3}}
\\hypersetup{{colorlinks,breaklinks,
            linkcolor=darkblue,urlcolor=darkblue,
            anchorcolor=darkblue,citecolor=darkblue}}

% Name Goes Here
\\name{{{data['name']}}}

% Contact Stuff Goes Here
\\address {{
"""

for i, v in enumerate(data['contact_info']):
    if i != 0:
        out += f"\t$\\cdot$ \\raisebox{{-0.0\\height}} {v}\n"
    else:
        out += f"\t\\raisebox{{-0.0\\height}} {v}\n"

out += "}\n\n\n"

out += "\\begin{document}\n\n\n"

# Profesional Overivew
out += "%Professional Overview\n"
out += "\\begin{rSection2}{Professional Overview}\n"
for i in data['professional_overview']:
    out += f"\t\\item {i}\n"
out += "\\end{rSection2}\n\n"


# Technical Strengths Section
out += """
%----------------------------------------------------------------------------------------
%	TECHNICAL STRENGTHS SECTION
%----------------------------------------------------------------------------------------

\\begin{rSection}{Technical Skills}
    \\begin{tabular}{ @{} >{\\bfseries}l @{\\hspace{6ex}} l }
"""

## Solution Stack
line, fl = str(), True
for i in data['technical_skills']['solution_stack']:
    if len(line) + len(i) + 2 <= MAX_SKILLS_LEN:
        line = line + i + ', '
    elif fl:
        out += ('\t\tSolution Stack & ' + line + '\\\\\n')
        line, fl = '& ' +  i + ', ', False
    else:
        out += ('\t\t' + line + '\\\\\n')
        line = '& ' + i + ', '
out += ('\t\t' + line[:-2] + '\\\\\n')

# Software/Tools
line, fl = str(), True
for i in data['technical_skills']['software_tools']:
    if len(line) + len(i) + 2 <= MAX_SKILLS_LEN:
        line = line + i + ', '
    elif fl:
        out += ('\t\tSoftware/Tools & ' + line + '\\\\\n')
        line, fl = '& ' +  i + ', ', False
    else:
        out += ('\t\t' + line + '\\\\\n')
        line = '& ' + i + ', '
out += ('\t\t' + line[:-2] + '\\\\\n')


out += """\t\\end{tabular}
\\end{rSection}


"""



out += "\\end{document}"

# Write output to file
with open('output/raw_tex/resume.tex', 'w') as outfile:
    outfile.write(out)