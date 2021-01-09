import string

content = []
corrcontent = []
occurrences = []

choosefile = input("Choose a file: ")
file = str(choosefile) + ".html"

with open(file,'rt', encoding="utf8") as file: #Opens the text file as a read-only text file
	
    for line in file:
        indexs = line.find(">")
        indexf = line.find("</")
        wordcontent = line[indexs+1:indexf]
        for word in wordcontent.split():
            content.append(word) #splits up file into individual words and adds each one to the first list.

for t in content:
    out = t.translate(str.maketrans("","", string.punctuation)) #Filters out puntuation from each element in the list
    corrcontent.append(out + " : ") #The filtered text file is now added into a new list, string by string. Colon is used to seperate occurrenace counter

corrcontent.sort() #sorting the list to make it easier to compare later

#Using a nested loop to compare common occurrences
for i in corrcontent:
    countoc = 0

    for j in corrcontent:
        if i == j:
            countoc += 1 #Iterate for first occurrence, and any other following it

        else:
            if countoc > 2:
                a = i + str(countoc) #variable containing the word. and the amount of occurrences it had if more than 3
                occurrences.append(a) #Add this concatenated string to our new array
                occurrences = list(dict.fromkeys(occurrences))  # filter out duplicate string elements
            countoc = 0 #Reset to 0 if no more identical occurrences

print("\nSelected file: " + str(file) + "\n")

#f = open(str(choosefile) + "_word_sorted.txt", "w")
#f.write(str(occurrences))
#f.close()
with open (str(choosefile) + "_word_sorted.txt", 'w', encoding="utf8") as f:
	print(*occurrences, sep='\n', file=f)
print("Saved to file: " + str(choosefile) + "_word_sorted.txt")