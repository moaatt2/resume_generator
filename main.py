
start = """
%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\\documentclass{resume}
% Use the custom resume.cls style

\\usepackage{fontawesome5}
\\usepackage{amsmath}
\\usepackage{tabularx}
\\usepackage{scalerel}

\\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{geometry} % Document margins
\\newcommand{\\tab}[1]{\\hspace{.2667\\textwidth}\\rlap{#1}}
\\newcommand{\\itab}[1]{\\hspace{0em}\\rlap{#1}}

\\usepackage{color,hyperref}
\\definecolor{darkblue}{rgb}{0.0,0.0,0.3}
\\hypersetup{colorlinks,breaklinks,
            linkcolor=darkblue,urlcolor=darkblue,
            anchorcolor=darkblue,citecolor=darkblue}
"""

with open('output/raw_tex/resume.tex', 'w') as outfile:
    outfile.write(start)