#!/usr/bin/python2
import socket
recv_port=8888
recv_ip="127.0.0.1"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
choice=raw_input("1 for both way communication and 2 for single way only ")
if choice == "1":
	while(1):
		msg=raw_input("Enter your message")
		s.sendto(msg,(recv_ip,recv_port))
		print(s.recvfrom(100))
elif choice == "2":
	while(1):
		msg=raw_input("enter your msg")
		s.sendto(msg,(recv_ip,recv_port))
else:
	print("Invalid choice")
