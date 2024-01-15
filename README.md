# Resume Generator

## Overview

The purpose of this project is to generate multiple variations of a resume while pulling from a single source of truth.


## Attribution

The base resume template is based on Trey Hunner's LaTeX resume template(found [here](https://github.com/treyhunner/resume/tree/master)).

## How To Use This Tool

To use this tools follow the steps below:
1. Install the python requirements in the requirements file.
2. Ensure that you have latex installed and can run the `pdflatex` command in your console.
3. Create a data file following one of the formats laid out below.
4. Update line 11 of `main.py` with the name of the file.
5. Create a folder called `output` with the subfolders `compiled_results` and `raw_tex` at the same level as `main.py`.
6. Run the script `main.py` and find your resumes in `output/compiled_results`.


## Data File Formats

A single `YAML` or `JSON` data file can represent either a single resume or multiple resuemes depending on the format. Please consult the appropriate reference to determine the correct format for your file.

### Single Version

The YAML spec is:

```YAML
name: John Doe # The name that you want at the top of the resume
contact_info: # A list of contact info latex snippets to go under the name
    - 
professional_overview: # A list of short snippets going under the contact info
    - 
technical_skills:
    solution_stack: # A list of technical tools you are familiar with
        -
    software_tools: # A list of software/tools you are familar with
        -
education: # A list of education items like the one below
  - institution: Smallville College # The institution that granted the degree
    location: Smallville # Where the institution is located
    degree: Bachelors # What degree you got
    time: 2023 # When you got your degree
    points: # A list of points you would like to note about your education
        -
experience: # A list of job items like the one below
  - company: Corp Corp # The company you worked for
    location: Smallville # Where your job was located
    title: Worker # Your job title
    time: 2023-present # When you had the job
    points: # A list of points about the job
      - 
```

The JSON spec is:

```JSON
{
    "name": "The name that you want at the top of the resume", 
    "contact_info": ["A list of contact info latex snippets to go under the name"],
    "professional_overview": ["A list of short snippets going under the contact info"],
    "technical_skills": {
        "solution_stack": ["A list of technical tools you are familiar with"],
        "software_tools": ["A list of software/tools you are familar with"]
    },
    "education": [
        "A list of education items like the one below",
        {
            "institution": "The institution that granted the degree",
            "location": "Where the institution is located",
            "degree": "What degree you got",
            "time": "When you got your degree",
            "points": ["A list of points you would like to note about your education"]
        }
    ],
    "experience": [
        "A list of job items like the one below",
        {
            "company": "The company you worked for",
            "location": "Where your job was located",
            "title": "Your job title",
            "time": "When you had the job",
            "points": ["# A list of points about the job"]
        }
    ]
}
```

### Multi Version

#TODO