opennebula-integration

This folder contains the files for opennebula integration using XML RPC project.

Code Tested on Python 3.5.2

Requirements 
 - python-oca :Python opennebula cloud binding
   1. Download the source from 
	https://pypi.python.org/packages/af/53/2ddbdb30dc5992c969e82203e494358da328d265a0a78931b73e4ceb7a70/oca-4.10.0.tar.gz#md5=9ec5e6c09fe293f7a5f2dab2719bedc2
	OR
   Get the source from github
	https://github.com/python-oca/python-oca

   2. Then execute the following in the python-oca source folder
	python setup.py build
	sudo python setup.py install
	

Running the script
   1. Make sure you create a config.py file from config.py.sample file, by copying it and changing the parameters according to the OpenNebula infrastructure.
   2. Run the python script.
	python CreateVM.py

   This will create a VM of 128 MB and 1 Processor on the OpenNebula. 
