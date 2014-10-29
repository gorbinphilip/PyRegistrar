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
