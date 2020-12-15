import re
import sys
from numpy import savetxt
from os.path import abspath

a = 0

expressions = []

while (a == 0):

	userchoice = input("Which file would you like to read from?")

	textfile = str(userchoice) + ".html"

	file = open(textfile,"rt", encoding='utf8') #Opening the file with utf8 so all the characters are read properly
	content = file.read()

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


print("Regular Expression Results")
for i in range(len(regexps)):
	r1 = re.findall(regexps[i],content)
	resnum = i + 1
	expressions.append("Result " + str(resnum) + " from " + regexps[i] + ": ")
	expressions.append(r1)

print("Multi-Line Expression Results")
for j in range(len(multilineexps)):
	r2 = re.findall(multilineexps[j],content,re.MULTILINE)
	mulnum = j + 1
	expressions.append("Result " + str(mulnum) + " from " + multilineexps[j] + ": ")
	expressions.append(r2)

#Save to File (userhoice + "_Regex_Results")

#expressions.astype("int8").tofile(str(choosefile) + "_word_sorted.txt")
savetxt(str(userchoice) + "_regex_results.txt", expressions, delimiter=',')
print("Saved to file: " + str(userchoice) + "_regex_results.txt")