text = input("Enter a String: ").split()
acronym = ""
for i in text:
	acronym = acronym + i[0].upper()
print(acronym)