
#!/usr/bin/python3
import datetime
name=input("Enter your name")
age=int(input("enter your age"))
var= datetime.datetime.now()
print(name + "will be of 95 yrs old by the year :"+str((95-age)+var.year))

