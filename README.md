# Project Structure

The directory is divided in sub-folders. Each of which contains the relative source code. Just clone this repository on your computer or Fork it on GitHub. Find out more on how to get started [here](https://youtu.be/iueBeWkLq60).

## `./data` folder

The objective of this folder is to share publicly data with other researchers.

>It **SHOULD NOT** contain identifiable data. 

## `./code` folder

Please save your source code in the `code` folder. 

> Figures and Tables to be used in the manuscript should be saved in the  respective folder `manuscript/src/figures` or `manuscript/src/tables`

## `./src` folder

Contains the LaTeX files

## LaTeX files 

[main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex) is the source file that your Latex compiler will use to generate the paper. However, in order to keep the code cleaner, the main sections of the paper are all located in the [sections](https://github.com/FedericoTartarini/reproducible-research/tree/master/manuscript/src/sections). In this way you will experience less merging issues when two or more people are working on the same manuscript.

### Sections

To add a new section just copy a section file (e.g., [introduction.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/sections/introduction.tex)) paste it in the same directory. Rename the pasted file (e.g. discussion.tex) and add this file to [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex).

[Chapters and sections - video tutorial](https://youtu.be/rM0Gk_DadWA)

### Figures

Import them from the `figures` folder using the `\includegraphics{}` command. [Figures - video tutorial](https://youtu.be/jg4t0xFDbdk)

### Tables

Import them from the `figures` folder using the `\input{}` command. 
* [Tables - Video tutorial](https://youtu.be/-sRYdfYMuhE)
* [How to use include command](https://youtu.be/V_eCCNlBuMo)

### Equations

[Equations - video tutorial](https://youtu.be/V4htbZeDUMU)

### Cite a document

[How to cite a document - video tutorial](https://youtu.be/cetKX6gWAIo)

### Code Listing

[Code listing - video tutorial](https://youtu.be/ByduYnAu2jM)

### Changing template

For your convenience I have already included the Elsevier Latex template at the beginning of the [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex). Feel free to change that.

# Style guide and useful notes

* I have added the nomenclature. Entries are defined in the `acronyms.tex` file and can be referenced in the text using the \ac{} command. [More info here](https://youtu.be/zPrWS5cnDgc)
* Write each sentence in a new line. To go in a new line (equivalent to using enter in Word) just leave an empty row between two sentences.
* ~ are non-breaking spaces.
* to leave a comment, go in a new line then type `% todo ....` (replace the dots with your comment)

# Prerequisites

## Data Analysis Software

Python or R for the data analysis, but you can also use other programming languages or tools

## Latex

Latex IDE and compiler installed locally on your machine. I recommend using a PyCharm plugin called [TeXiFy IDEA](https://plugins.jetbrains.com/plugin/9473-texify-idea) as IDE and [miktex](https://miktex.org) as Latex compiler. [How to install TeXiFy](https://youtu.be/bxXMZV9f9P8)

Alternatively you can push your code to Overleaf using git and only use Overleaf. I would discourage you from doing this! [Overleaf - video tutorial](https://youtu.be/E84AeZUlv8s)

## Git and Git Web Hosting

You should install [git](https://git-scm.com) on your computer. And have [GitHub](https://github.com) or [GitLab](https://about.gitlab.com) account

## IDE

You may want to take advantage of the power of IDEs. Well as you all know my preferred choice are [JET Brains IDEs](https://www.jetbrains.com/products.html) and for Python and R I would recommend using [PyCharm](https://www.jetbrains.com/pycharm/). Alternatives are:

* [visual Studio (VS) code](https://code.visualstudio.com)
* [RStudio](https://rstudio.com)

# Additional Resources

* [LaTeX - video tutorials](https://youtube.com/playlist?list=PLY91jl6VVD7wnyOlAgPRe-i9ov4_ZqHV8)
* [Overleaf Tutorial website](https://www.overleaf.com/learn/latex/Tutorials) 
* [Latex wikibooks](https://en.wikibooks.org/wiki/LaTeX).