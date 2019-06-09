import datetime

name =input("Enter your Name ")
var=datetime.datetime.now()
if var.hour in range(4,12):
	print("Good Morning",name)
elif var.hour in range(12,17):
	print("Good Afternoon",name)
elif var.hour in range(17,22):
	print("Good Evening",name)
else:
	print("Good Night", name)
