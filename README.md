# Reproducible research

This repository gives you an example on how you can structure your research project, from the data analysis all the way to the final version of the manuscript or a presentation.

The overarching aim is:
* to make our research more reproducible so other researchers can re-use our code, data;
* to speed up review process (e.g., avoiding that we use different tools which are not 100% compatible, Google Form, Word, etc)
* to minimise errors (e.g., copying and pasting values in Word tables and PowerPoint)

For this purpose I have tried to leverage the best tools that there are currently out there (at least in my opinion) and I have put together this repository which could be used as template/starting point to ensure that we follow a more structured approach in research. It leverages the power of Python, R and Latex, to streamline the data analysis and publication process.  

This project is still in Beta version, hence it is far from being complete and the file structure may soon change. Please feel free to contribute.

## Table of content 

-   [Getting Started](#getting-started)
    -   [Data](#source-data)
    -   [Data Analysis](#data-analysis)
    -   [Manuscript and Presentation](#manuscript-and-presentation)
        -   [Manuscript](#manuscript)
            -   [Adding new section](#adding-a-new-section)
            -   [Figures, Tables, Equations](#figures-tables-or-math-equations)
            -   [Changing Template](#changing-template)
        -   [Additional resources](#additional-resources)
-   [Prerequisites](#prerequisites)
    -   [Data Analysis Softwares](#data-analysis-software)
    -   [Latex](#latex)
-   [Useful Resources](#useful-resources)
    -   [Databases](#open-source-databases)
    -   [IDE](#ide)
    -   [Git](#git-and-git-web-hosting)
-   [Author](#authors)
-   [Licence](#license)

## Getting Started

The directory is divided in sub-folders. Each of which contains the relative source code. Just clone this repository on your computer or Fork it on GitHub

### Source Data

The objective of this folder is not to replace the database, but instead to share only some of the database data with other researchers. Data should only contain the .csv files that you want to share publicly. 

>It **SHOULD NOT** containc identifiable data. 

### Data Analysis

Please save your source code in the `code` folder. Currently you can find an example of a Python, R and Jupiter notebook in this folder.

> Figures and Tables to be used in the manuscript should be saved in the  respective folder `manuscript/src/figures` or `manuscript/src/tables`

Once you have finalized your research, your data should then be saved in [Dryad](https://datadryad.org/stash/): Dryad is an open-source, research data curation and publication platform. Datasets published in Dryad receive a citation and can be versioned at any time. You can [upload your data on Dryad](https://datadryad.org/stash/submission_process#upload-methods) by copy and pasting in their system the GitHub URL.

If your code needs to connect to a database or a server please make sure the `username` and `password` are not saved in plain text in your code. I keep my password saved in a file called `secret.py` and added this file to [.gitignore](https://github.com/FedericoTartarini/reproducible-research/blob/master/.gitignore) so this file is not synced to the GitHub repos. And then import this file at the beginning of my `main.py` file.

> Make sure you save the data you imported from the database in the [Data](#source-data) folder so other researchers can import the raw data if they want to reproduce your results. Alteratively write a script which pulls the data from Dryad.

### Manuscript and Presentation

The manuscript contains all the Latex files needed to generate your manuscript and your presentation. The main source files are located in the `manuscript/src`.

* [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex) is your manuscript source file. The final PDF can be found [here](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/presentation_out/presentation.pdf).
* [Presentation.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/presentation.tex) contains the code to generate your presentation. The final PDF can be found [here](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/out/main.pdf).

#### Manuscript 

[main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex) is the source file that your Latex compiler will use to generate the paper. However, in order to keep the code cleaner, the main sections of the paper are all located in the [sections](https://github.com/FedericoTartarini/reproducible-research/tree/master/manuscript/src/sections). In this way you will experience less merging issues when two or more people are working on the same manuscript.

Just edit the text in the relative Latex file (e.g., introduction, methodology, etc.) and you should be ready to go. No need to change any other file.

##### Adding a new section

Just copy a section file (e.g., [introduction.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/sections/introduction.tex)) paste it in the same directory. Rename the pasted file (e.g. discussion.tex) and add this file to [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex).

##### Figures, Tables or Math equations

See the boilerplate code in [results.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/sections/results.tex).

##### Changing template

For your convenience I have already included the Elsevier Latex template at the beginning of the [main.tex](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/main.tex). Feel free to change that.

If you choose to use the Elsevier template you can change the bibliography style in the [mypreamble.sty](https://github.com/FedericoTartarini/reproducible-research/blob/master/manuscript/src/mypreamble.sty) file.

#### Additional Resources

Alternatively you can find great resources on the [Overleaf Tutorial website](https://www.overleaf.com/learn/latex/Tutorials) or on [Latex wikibooks](https://en.wikibooks.org/wiki/LaTeX).

### Prerequisites

#### Data Analysis Software

Python or R for the data analysis, but you can also use other programming languages or tools such as Energy Plus. How to get you started with this tools is outside the scope of this repository, but you can find a million videos on YouTube or tutorials on the Internet.

> I would highly recommend you using an IDE to write code, see more below.

#### Latex

Latex IDE and compiler installed locally on your machine. I recommend using a PyCharm plugin called [TeXiFy IDEA](https://plugins.jetbrains.com/plugin/9473-texify-idea) as IDE and [miktex](https://miktex.org) as Latex compiler  

Alternatively you can push your code to Overleaf using git and only use Overleaf. I would discourage you from doing this! Overleaf should only be used for the review.

## Useful Resources

### Open Source Databases

If you are not sure about which database to choose and you are a researcher, in 80-90% of the cases you should be fine with an SQL database, alternatively you may want to use a Time Series database.

#### SQL
 
* [PostgreSQL](https://www.postgresql.org)
* [mySQL](https://dev.mysql.com/doc/mysql-getting-started/en/)

#### No SQL

* [Mongo DB](https://www.mongodb.com)

### IDE

You may want to take advantage of the power of IDEs. Well as you all know my preferred choice are [JET Brains IDEs](https://www.jetbrains.com/products.html) and for Python and R I would recommend using [PyCharm](https://www.jetbrains.com/pycharm/). Alternatives are:

* [visual Studio (VS) code](https://code.visualstudio.com)
* [RStudio](https://rstudio.com)

> Always think about the future, if you think you may start doing a bit of Web development, App development (Android, Apple) or Software. The best options are PyCharm of VS Code.

I personally think you should not use Jupiter Notebook, but feel free to use it if you like it. 

### Git and Git Web Hosting

You should install [git](https://git-scm.com) on your computer. And have [GitHub](https://github.com) or [GitLab](https://about.gitlab.com) account

## Authors

* **[Federico Tartarini](https://github.com/FedericoTartarini)** - *Initial work*

See also the list of [contributors](https://github.com/FedericoTartarini/reproducible-research/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## CHANGELOG
