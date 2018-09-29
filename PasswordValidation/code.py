import re 
password =input()
if not re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password):
	print("InValid Password") 

else: 
	print("Valid Password") 
