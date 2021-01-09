import re
import sys
from os.path import abspath

a = 0

expressions = []

while (a == 0):

	userchoice = input("Which file would you like to read from?")

	textfile = str(userchoice) + ".html"

	print("Chosen File: " + str(textfile) + "\n")

	regexps = []
	multilineexps = []
	c = 0

	while (c == 0):
		exp = input("Enter a regular expression: ")

		response = input("Is this a multiple line expression?")

		if (response == "yes"):
			multilineexps.append(exp)
		else:
			regexps.append(exp)

		confirmexp = input("Would you like to add another expression? ")
		if (confirmexp == "yes"):
			c = 0
		else:
			c = 1

	print("Regular Expressions Added: "+ str(regexps))
	print("Multi-Line Expressions Added: "+ str(multilineexps))

	confirm = input("Proceed with Regex Execution?")

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

	with open(textfile, 'rt', encoding="utf8") as file:  # Opens the text file as a read-only text file
		resnum = 0
		for line in file:
			indexs = line.find(">")
			indexf = line.find("</")
			wordcontent = line[indexs + 1:indexf]

			resnum = resnum + 1


			for i in range(len(regexps)):
				r1 = re.findall(regexps[i],wordcontent)
				expressions.append("Line " + str(resnum) + " with " + regexps[i] + ": " )
				expressions.append(r1)


			for j in range(len(multilineexps)): #Not working properly
				continue
				r2 = re.findall(multilineexps[j],wordcontent,re.MULTILINE)
				mulnum = j + 1
				expressions.append("Result " + str(mulnum) + " from " + multilineexps[j] + ": ")
				expressions.append(r2)

		print("Regular Expression Results Added")

with open (str(userchoice) + "_regex_results.txt", 'w', encoding="utf8") as f:
	print(*expressions, sep='\n', file=f)
#f = open(str(userchoice) + "_regex_results.txt", "w")
#f.write(str(expressions))
#f.close()
print("Saved to file: " + str(userchoice) + "_regex_results.txt")