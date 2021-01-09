from os.path import abspath

comments = []

choosefile = input("Choose a file: ")
file = str(choosefile) + ".html"

with open(file,'rt', encoding="utf8") as file:

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

with open (str(choosefile) + "_html_comments.txt", 'w') as f:
	print(*comments, sep='\n', file=f)
#f = open(str(choosefile) + "_html_comments.txt", "w")
#f.write(str(comments))
#f.close()
print("Saved to file: " + str(choosefile) + "_html_comments.txt")