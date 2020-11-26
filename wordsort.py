import string

content = []
corrcontent = []
occurrences = []

choosefile = input("Choose a file: ")
file = str(choosefile) + ".txt"
print("\nSelected file: " + str(file) + "\n")

with open(file,'rt') as file: #Opens the text file as a read-only text file
	
    for line in file:
        for word in line.split():
            content.append(word) #splits up file into individual words and adds each one to the first list.

for t in content:
    out = t.translate(str.maketrans("","", string.punctuation)) #Filters out puntuation from each element in the list
    corrcontent.append(out + ":") #The filtered text file is now added into a new list, string by string. Colon is used to seperate occurrenace counter

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

print(occurrences) #Prints finished list