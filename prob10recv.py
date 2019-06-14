#!/usr/bin/python2
import socket
recv_ip="127.0.0.1"	
recv_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
choice=raw_input("1 for both way communication and 2 for single way")
if choice == "1":
	while(1):
		data=s.recvfrom(100)
		print(data)
		msg=raw_input("Enter your reply")
		s.sendto(msg,data[1])
elif choice =="2" :
	while(1):
		print(s.recvfrom(100))
else:
	print("Invalid choice")
