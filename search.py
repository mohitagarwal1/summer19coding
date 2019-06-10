#!/usr/bin/python3
import webbrowser
from googlesearch import search
var=[]
data = input("Enter your search : ")
x=search(data,stop=10)
for i in x:
	var.append(i)
with open('stored_url.txt','w') as f:
	for i in var:
		f.write("%s\n" %i)
webbrowser.open("https://www.google.com/search?q="+data)
