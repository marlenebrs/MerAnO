[![PyPI version](https://img.shields.io/pypi/v/merano?style=plastic)](https://pypi.org/project/MerAnO/) [![GitHub license](https://img.shields.io/github/license/marlenebrs/MerAnO?style=plastic)](https://github.com/marlenebrs/MerAnO/blob/master/LICENSE) [![Actions Status](https://github.com/AuReMe/metage2metabo/workflows/Python%20package/badge.svg)](https://github.com/marlenebrs/MerAnO/actions) [![Documentation Status](https://img.shields.io/readthedocs/merano/latest?style=plastic)](https://merano.readthedocs.io/en/latest/)
# MerAnO
MerAnO is a python3 package created as part of the Bioinformatics master's degree in Bordeaux. MerAnO for "Merge & Analyze Organism" has two separate objectives.
 
 * Merge files in SBML format while modifying the identifiers. Thus, each "species" or "reaction" present in the final file is associated with an organism.
 * Analyze the modules present in a file in annotation format. The data required in KEGG allows the development of graphs illustrating the proportion of modules in each organization and compares the modules of the organizations included in the analysis.


## Table of contents
- [MerAnO](#merano)
  - [Table of contents](#table-of-contents)
  - [License](#license)
  - [Documentation](#documentation)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Installation with pip](#installation-with-pip)
  - [Features](#features)
  - [Release Notes](#release-notes)
  - [Authors](#authors)
  - [Acknowledgement](#acknowledgement)


## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://github.com/marlenebrs/MerAnO/blob/master/LICENSE) file for details.

## Documentation

A more detailled documentation is available at: [https://merano.readthedocs.io](https://merano.readthedocs.io/en/latest/).

## Technologies

Python 3 (Python 3.8 is tested). MerAnO uses a certain number of Python dependencies. A list of the dependencies working for MacOs (version ???) and Linus (???) is available in [requirements.txt](https://github.com/marlenebrs/MerAnO/blob/master/requirements.txt).

They can be installed with:
````sh
pip install -r requirements.txt 
````

## Installation

Tested on Linux (???) and MacOs (version ???).
Tested with Python3.8

### Installation with pip

```
pip install MerAnO
```

## Features

````
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
merano is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


usage: merano [-h] [-m SBML_files] [-a Annotation_files]

At least one optional argument is required

Merge several SBML files to get a general overview of metabolic network. Generate basic statistics about a set of organisms.

optional arguments:
  -a                    get basic statistics from annotation
                        files in input
  -h                    show this help message and exit
  -m                    merge the SBML documents in input

````



## Release Notes

Changes between version are listed on the [release page](https://github.com/marlenebrs/MerAnO/releases).



## Authors
[Marie Ancelle](https://github.com/Marie-Ancelle), [Marlène Barus](https://github.com/marlenebrs), [Mathilde Borg](https://github.com/mathildeborg), [Céline Mathez](https://github.com/cmathez) and [Marieke Paardekooper](https://github.com/MariekeLP), Univ Bordeaux, Master Bioinformatique, du Génome aux Ecosystemes, Bordeaux, France.

## Acknowledgement
**Clémence Frioux** (inria, Bordeaux) for suggesting this project as a part of our master's program and for her highly formative support throughout the project.
