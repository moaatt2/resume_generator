
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Copying and distribution of this file, with or without modification,
% are permitted in any medium without royalty provided the copyright
% notice and this notice are preserved.  This file is offered as-is,
% without any warranty.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ProvidesClass{resume}[2010/07/10 v0.9 Resume class]

\LoadClass[11pt,letter]{article}

\usepackage[parfill]{parskip}       % Do not indent paragraphs
\usepackage{array}                  % required for boldface tabular columns
\usepackage{ifthen}

\nofiles                            % .aux files are not needed for resumes
\pagestyle{empty}                   % resumes do not need page numbers

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% HEADINGS: Commands for printing name and address

\def \name#1{\def\@name{#1}}        % \name command can be used to set name
\def \@name {}                      % Set \@name to empty by default

\def \addressSep {$\diamond$}         % Set default address seperator

% One or two address lines can be specified
\let \@addressone \relax
\let \@addresstwo \relax

% \address command can be used to set first and second address (optional)
\def \address #1{
  \@ifundefined{@addresstwo}{
    \def \@addresstwo {#1}
  }{
    \def \@addressone {#1}
  }
}

% \printaddress is used to style an address line (given as input)
\def \printaddress #1{
  \begingroup
    \def \\ {\addressSep\ }
    \centerline{#1}
  \endgroup
  \par
  \addressskip
}

% \printname is used to print the name as a page header
\def \printname {
  \begingroup
    \hfil{\MakeUppercase{\namesize\bf \@name}}\hfil
    \nameskip\break
  \endgroup
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DOCUMENT: Create the head of the document

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document                     % Begin document
  \printname                        % Print the name specified with \name
  \@ifundefined{@addressone}{}{     % Print the first address if specified
    \printaddress{\@addressone}}
  \@ifundefined{@addresstwo}{}{     % Print the second address if specified
    \printaddress{\@addresstwo}}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SECTIONS: Create section headings

% Used to create large resume section
\newenvironment{rSection}[1]{
  \sectionskip
  \MakeUppercase{\bf #1}
  \sectionlineskip
  \hrule
  \sectionlineskip
  \begin{list}{}{
    \setlength{\leftmargin}{1.5em}
  }
  \item[]
}{
  \end{list}
}


\newenvironment{rSection2}[1]{
  \sectionskip
  \MakeUppercase{\bf #1}
  \sectionlineskip
  \hrule
  \sectionlineskip
  \smallskip
  % \cdot used for bullets, items non-indented
  \begin{list}{$\cdot$}{\leftmargin=2em}
  \itemsep -0.5em \vspace{-0.5em}
}{
  \end{list}
  \vspace{0.5em}
}






\newenvironment{rEducation}[5]
{
  {\bf #1,} {#2} \hfill {#3}
  \ifthenelse{\equal{#4}{}}{}{
  \\
  {\em #4} \hfill {#5}
  }
    \vspace{0.5em}
}


% Used to format job listing
\newenvironment{rSubsection}[5]{
  %%%%%%%%%%%%%%%%%%%%%% Default Layout: %%%%%%%%%%%%%%%%%%%%%%%%
  %%    Employer (bold), Location           Dates (regular)    %%
  %%    Title (emphasis)                    other              %%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  {\bf #1} {#2} \hfill {#3}
  \ifthenelse{\equal{#4}{}}{}{
  \\
  {\em #4} \hfill {#5}
  }
  \smallskip
  % \cdot used for bullets, items non-indented
  \begin{list}{$\cdot$}{\leftmargin=2em}
  \itemsep -0.5em \vspace{-0.5em}
}{
  \end{list}
  \vspace{0.5em}
}



\newenvironment{rStackedSubsection}[7]
  %%%%%%%%%%%%%%%%%%%%%% Default Layout: %%%%%%%%%%%%%%%%%%%%%%%%
  %%    Employer (bold), Location                              %%
  %%    Title (emphasis)                    Dates (regular)    %%
  %%    Title (emphasis)                    Dates (regular)    %%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
{
  {\bf #1,} {#2} \hfill {#3}
%
  \ifthenelse{\equal{#4}{}}{}{
  \\
  {\em #4} \hfill {#5}
  }
%
  \ifthenelse{\equal{#6}{}}{}{
  \\
  {\em #6} \hfill {#7}
  }
%
  \smallskip
  \begin{list}{$\cdot$}{\leftmargin=2em}
  \itemsep -0.5em \vspace{-0.5em}
}
{
  \end{list}
  \vspace{0.5em}
}











\def\namesize{\huge}
\def\nameskip{\medskip}
\def\addressskip{\smallskip}
\def\sectionskip{\bigskip}
\def\sectionlineskip{\medskip}










