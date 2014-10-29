PyRegistrar
===========

A console based application that accepts details of any configured
object and exports those data in different file formats.

One of the default model "Alien" is implemented on the following aspect:

Aliens on Earth:
---------------- 
A treaty of friendship has been signed between Aliens and Humans. The
aliens are now welcome on Earth and can stay as long as they wish with
the Humans. Here pyregistrar can be used to create document based on
the 'Alien' model.

Usage:
------
	register [-h] [-f] [-e] [-m]
	 
	 -h: shows command help
	 -f filename  : specify output file name. Generates a random
            	      	filename by default.
	 -e extension : specify output file format. Uses 'plain'
            	      	extension by default.
	 -m model     : specify model to be used. 'Alien' is used as
            	      	default.


Installation:
---------
Goto project directory "PyRegistrar"  where setup.py is located. Then type,

     python setup.py install


Development:
------------
Models:

Custom models can be added to 'pyregistrar.models' by implementing
Model and adding it to the global var __all_models__. Model should
specify attributes using the Field from fields.

Extensions:

Custom extensions can be implemented by placing new extension into
'pyregistrar.extensions'. It is mandatory to make sure that the
extension added should obey the following constraints.

       	  module: any qualified module name.
       	  class : Export(), no arguments.
       	  method: export(data_list, file_name), where data_list will get
       	       	  iterable list of 2 tuples as key and attribute and file_name
      	      	  will receive absolute name for the file to be created.