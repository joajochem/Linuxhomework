#!/usr/bin/env python3


with open('local-host-names','a+r') as f:
	f_contents = f.read()
	print(f_contents)
	
	f_contents.write("testdomein.nl")

#with open('test.txt', 'w') as file:
#	file.write(f_contents)
	
