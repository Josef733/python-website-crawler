import re
import sys
import scrapy

#Init
a = 0

while (a == 0):
	
	url = input("Enter the URL for crawling: ")
	level = int(input("Enter the depth of crawling (help in readme): "))
	
	regexps = []
	b = 0

	add = input("Would you like to add any regular expressions? ")

	if (add == "yes"):
		while (b == 0):
			exp = input("Enter a regular expression: ")
			regexps.append(exp)
			confirmexp = input("Would you like to add another expression? ")
			if (confirmexp == "yes"):
				b = 0
			else:
				b = 1

	print("Selected Parameters:\n")
	print("URL: " + url)
	print("Crawling Depth: " + str(level))
	print("Regular Expressions: "+ str(regexps))
	confirm = input("Proceed with website crawling (yes/no)? ")

	if (confirm == "yes"):
		a = 1

	elif (confirm == "no"):
		restart = input("Would you like to restart? ")
		if (restart == "yes"):
			a = 0
		else:
			sys.exit()
	else:
		sys.exit()

#Main
print("Starting...")


#Output/Downloads

print("Complete!")