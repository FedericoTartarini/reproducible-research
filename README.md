# Reproducible research

This repository gives you an example on how you can structure your research project, from the data analysis all the way to the final version of the manuscript or a presentation.

Alternatively you could also look at [this repository](https://github.com/CenterForTheBuiltEnvironment/rmd-example) titled: "A reproducible journal article template in RMarkdown" put together by our colleagues at CBE.

-   [Getting Started](#getting-started)
    -   [Data](#data)
    -   [Manuscript and Presentation](#manuscript-and-presentation)
        - [Manuscript](#manuscript)
            - [Adding new section](#adding-a-new-section)
            - [Figures, Tables, Equations](#figures-tables-or-math-equations)
-   [Prerequisites](#prerequisites)

## Getting Started

The directory is divided in sub-folders. Each of which contains the relative source code.

### Data

Data should only contain the .csv files that you want to share publicly. 


>It **SHOULD NOT** contain identifiable data. The objective of this folder is not to replace the database, but instead to share some of the database data with other researchers

### Manuscript and Presentation

The manuscript contains all the Latex files needed to generate your manuscript and your presentation. The main source files are located in the `manuscript/src`.

* [Presentation.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/presentation.tex) contains the code to generate your manuscript.
* [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex) is your manuscript source file.

#### Manuscript 

[main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex) is the source file that your Latex compiler will use to generate the paper. However, in order to keep the code cleaner, the main sections of the paper are all located in the [sections](https://github.com/FedericoTartarini/reproducible-research/tree/master/manuscript/src/sections). In this way you will experience less merging issues when two or more people are working on the same manuscript.

Just edit the text in the relative Latex file (e.g., introduction, methodology, etc.) and you should be ready to go. No need to change any other file.

##### Adding a new section

Just copy a section file (e.g., [introduction.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/sections/introduction.tex)) paste it in the same directory. Rename the pasted file (e.g. discussion.tex) and add this file to [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex).

##### Figures, Tables or Math equations

See the boilerplate code in [results.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/sections/results.tex).

Alternatively you can find great resources on the [Overleaf Tutorial website](https://www.overleaf.com/learn/latex/Tutorials) or on [Latex wikibooks](https://en.wikibooks.org/wiki/LaTeX).



## More Information

Each folder contains a README file with detailed informations.

### Prerequisites

Python or R for the data analysis.

Latex compiler if you want to compile your file locally.

### Installing

Just clone this repository on your computer or Fork it on GitHub

## Authors

* **[Federico Tartarini](https://github.com/FedericoTartarini)** - *Initial work*

See also the list of [contributors](https://github.com/FedericoTartarini/reproducible-research/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## CHANGELOG
