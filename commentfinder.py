from numpy import savetxt
from os.path import abspath

comments = []

choosefile = input("Choose a file: ")
file = str(choosefile) + ".html"

with open(file,'rt') as file:

	number = 0
	for line in file:
		number = number + 1
		index = line.find("<!--")
		comment = line[index:]
		print("Comment on line " + str(number) + " " +comment)

		identifier = "<!--"

		if identifier in line:
			comments.append("Comment on line " + str(number) + " " + comment)
			print("Added to list.\n")

print("Done.")
print(comments)
savetxt(str(choosefile) + "_html_comments.txt", comments, delimiter=',')
print("Saved to file: " + str(choosefile) + "_html_comments.txt")