import re
from numpy import savetxt

emailslist = []

choosefile = input("Choose a file: ")
htmlfile = str(choosefile) + ".html"
file = open(htmlfile,"rt", encoding='utf8') #Opening the file with utf8 so all the characters are read properly
content = file.read()

emails1 = re.findall("(\w*\d*@\w*.\w{2,4})",content,re.MULTILINE)
emails2 = re.findall("\w*\d*@\w*\w[.]\w*\w[.]\w{2,4}",content,re.MULTILINE)
print("Format 1 (name@domain.tld): " + str(emails1))
print("Format 2 (name@domain.subtld.tld): " + str(emails2))

emailslist.append("Format 1 (name@domain.tld): " + str(emails1))
emailslist.append("Format 2 (name@domain.subtld.tld): " + str(emails2))

print(emailslist)

savetxt(str(choosefile) + "_email_list.txt", emailslist, delimiter=',')
print("Saved to file: " + str(choosefile) + "_email_list.txt")