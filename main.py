
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
out += "\\end{rSection2}\n\n\n"
out += "\\end{document}"

# Write output to file
with open('output/raw_tex/resume.tex', 'w') as outfile:
    outfile.write(out)
