import re
import sys
import scrapy

#Init
a = 0

while (a == 0):
	
	urls = []
	b = 0

	while(b == 0):
		url = input("Enter the URL for crawling: ")
		urls.append(url)
		confirmurl = input("Would you like to add another address? ")
		if (confirmurl == "yes"):
			b = 0
		else:
			b = 1

	level = int(input("Enter the depth of crawling (help in readme): "))
	
	regexps = []
	c = 0

	add = input("Would you like to add any regular expressions? ")

	if (add == "yes"):
		while (c == 0):
			exp = input("Enter a regular expression: ")
			regexps.append(exp)
			confirmexp = input("Would you like to add another expression? ")
			if (confirmexp == "yes"):
				c = 0
			else:
				c = 1

	print("Selected Parameters:\n")
	print("URLs: " + str(urls))
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