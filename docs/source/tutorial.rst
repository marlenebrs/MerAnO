===============
MerAnO Tutorial
===============


Inputs
-------

**MerAnO**  offers two axes to process different types of data.
Run ``merano --help`` for information about the arguments

-m directory         directory of SBML files to merge
-a directory         directory of annotations files



To run this program you can choose either one or both options, however at least one is requiered.Whichever option is chosen, the full directory path must be mentioned for each option.
 * SBML files merge :
	The directory must exclusively contain files in ``.xml`` format.
	
	At least two files must be in the directory. As many files as possible are authorized but the program will slow down.

 * annotation files analyze :
	The directory must exclusively contain files in ``.fa.emapper.annotation`` format.
	
	Between 1 and 5 files must be in the directory. 

File format
-----------


Regarding the merging of SMBL files, inputs must conform to the SBML files regardless of the version. 
The format is in ``.xml``

For annotation files, the format is ``.fa.emapper.annotation``

Filename
---------

To have better results, it's important to check your filenames. This is how you should name them :

- SBML files

	*Genre_species_id.xml*

- Annotation files

	*Name.fa.emapper.annotation*


Outputs 
--------
- Storage

MerAnO creates a JSON file named modules.json and puts it in a Storage directory. To run correctly MerAnO, **! please don't modify this file !** but you can take it and work on it on another directory. 

- Results

The program creates a "Results" directory and places the output files in it.

* When using the "merge" argument, files are created: 

	* ``info.txt`` containing basic information for each organism.
	* ``merged_sbml.xml`` corresponding to merged files

* When using the "analyze" argument, files are created:
	
	* one png file per chart
	* pdf file with all charts and their descriptions




