#!/usr/bin/python3
import os
import crypt
var=input("enter username")
pswd="hello"+var
if var.isalpha():
    
    code=crypt.crypt(pswd,"22")
    os.system("sudo useradd -m -p "+code+" "+var)
    print("user created")
else:
	print("Enter valid username")
