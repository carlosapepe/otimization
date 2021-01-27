Tutorial for installing the lpsove library on linux

#-------------------------------------------------------------------------------------------------------------------------
Download the following two files from : https://sourceforge.net/projects/lpsolve/files/
lp_solve_5.5.2.0_dev_ux64.tar.gz - contains the .so files
lp_solve_5.5.2.0_Python2.5_exe_ux64.tar.gz - contains the python wrapper scripts for lpsolver,  which helps to invoke the native library from .so files. Unzip the above downloaded files, where each directory formed by unzip will have an lpsolve55.so file, though at different locations. Specify the paths to lpsolve55.so file in each directory by setting the following two environment variables:

export LD_LIBRARY_PATH=/usr/local/lib:/home/carlos/lp_solve_dev/

export LD_LIBRARY_PATH=/usr/lib/python2.7/lp_solve_dev

export PYTHONPATH=/home/carlor/usr/lib/python2.5/site-packages

export PYTHONPATH=/usr/lib/python2.7

#-------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------
Testing the lpsolve 
To test if lpsolver is configured as expected :
[xx-xxxx#ip-xx-x-x-xx ~]$ python
>>>Python 2.7.9 (default, Apr 1 2015, 18:18:03)
[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>from lpsolve55 import *
>>>lpsolve()
lpsolve Python Interface version 5.5.0.9
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
using lpsolve version 5.5.2.0
Usage: ret = lpsolve('functionname', arg1, arg2, ...)
#-------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------

Observation:

You need to play these two files:

lp_solve_dev/liblpsolve55.so  /usr/lib/python2.7

usr/lib/python2.5/site-packages/lpsolve55.so  /usr/lib/python2.7

Then  import:

from lp_solve import * (which acts as a python module)

And pass the parameters
#-------------------------------------------------------------------------------------------------------------------------

