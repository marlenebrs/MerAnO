===============
MerAnO Tutorial
===============


Inputs
-------

**MerAnO** program offers two axes for processing different data.
Run ``merano --help`` for knowing the arguments

-m directory         directory of SBML files to merge
-a directory         directory of annotations files


Whichever option is chosen, the full directory path must be mentioned. The latter must contain exclusively files in format ``.xml`` if you take the "merge" option and in format ``.fa.emapper.annotation`` if you take the "anayze" option.

File format
-----------


Regarding the merging of SMBL files, inputs must conform to the SBML files regardless of this version. 
The format is in ``.xml``

For annotation files, format is ``.fa.emapper.annotation``

Filename
---------

To have better results, it's important to check your filename. This is how you must named it :
- SBML files

	*Genre_species_id.xml*

- Annotation files

	*Name.fa.emapper.annotation*


Outputs 
--------
- Storage

MerAnO create a JSON file named modules.json and put it in Storage directory. To run correctly MerAnO, **Please don't modify this file** but you can take it and work on it on a other directory. 

- Results

The program creates a "Results" directory and places the output files in it.

* When using the "merge" argument, files are created: 

	* ``info.txt`` containing some information by organization.
	* ``merged_sbml.xml`` corresponding to merged files

* When using the "analyze" argument, files are created:
	
	* one png file by chart
	* pdf file with all charts and some description




