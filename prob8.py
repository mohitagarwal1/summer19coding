#!/usr/bin/python3
import os
import shutil
c_file=open('cmmndlist.txt','a+')
command=input("Enter command:")
c_file.write(command)
if(shutil.which(command)):
	os.system(command)
else:
	print("Not exist")
c_file.close()

