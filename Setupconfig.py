#!/usr/bin/env python3

import os



###################################
#input getter




#Default
#d_server = "boland.xs4all.nl"
#d_port = "443"
#d_name = "Joachim de Vos"
#d_email = "00125509@student.rocleiden.nl"


#customserver
def customserver():
	answercs = raw_input("Do you want to use default settings for server YES or NO:")
	if answercs == "YES":
		c_server = "boland.xs4all.nl"
		print(c_server)
		result = c_server
	elif answercs == "NO":		
		c_server = raw_input("Please enter Servername [boland.xs4all.nl]:")
		print(c_server)
		result = c_server
	return result

#customport
def customport():
	answercp = raw_input("Do you want to use default settings for port YES or NO:")
	if answercp == "YES":
		c_port = "443"
		print(c_port)
		result = c_port
	elif answercp == "NO":		
		c_port = raw_input("Please enter Servername [443]:")
		print(c_port)
		result = c_port
	return result
#customname
def customname():
	answercn = raw_input("Do you want to use default settings for port YES or NO:")
	if answercn == "YES":
		c_name = "Joachim de Vos"
		print(c_name)
		result = c_name
	elif answercn == "NO":		
		c_name = raw_input("Please enter your name")
		print(c_name)
		result = c_name
	return result
#custommail
def customemail():
	answerce = raw_input("Do you want to use default settings for port YES or NO:")
	if answerce == "YES":
		c_email = "00125509@student.rocleiden.nl"
		print(c_email)
		result = c_email
	elif answerce == "NO":		
		c_email = raw_input("Please enter email [00125509@student.rocleiden.nl]:")
		print(c_email)
		result = c_email
	return result


#replacer
###########################################

with open('email.conf','r+a') as f:
	f_contents = f.read()
	print(f_contents)
	c_server = customserver()
	c_port = customport()
	c_name = customname()
	c_email = customemail()
	
	f_contents = f_contents.replace('127.0.0.1', c_server)
	f_contents = f_contents.replace('25', c_port)
	f_contents = f_contents.replace('Your Real Name', c_name)
	f_contents = f_contents.replace('yourlogin@example.dmz', c_email)
	
	print(23*"=")
	print("                ")
	print("overview")
	print(23*"=")
	print(c_server)
	print(23*"=")
	print(c_port)
	print(23*"=")
	print(c_name)
	print(23*"=")
	print(c_email)
	print(23*"=")
	print(23*"=")
	
with open('email.conf', 'w') as file:
	file.write(f_contents)
	
