#concatenating strings
string="thirty"+" "+"days"+" "+"of"+" "+"python"
print(string)
#concatenating strings
string="Coding"+" "+"for"+" "+"all"
print(string)
#declaring a string variable
company="Coding For All"
#printing the string variable
print(company)
#length of the string
print(len(company))
#changing the string to uppercase
print(company.upper())
#changing the string to lowercase
print(company.lower())
#capitalizing the string
print(company.capitalize())
#title case the string
print(company.title())
#swap case the string
print(company.swapcase())
#slicing the string
print(company[0:6])
#searching for a word in the string
print(company.find("Coding"))
#replacing a word in the string
print(company.replace("Coding","Python"))
#spliting the string using space as a separator
print(company.split())
#splitting the string using comma as a separator
string="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))
#index 0 of the string
print(company[0])
#last index of the string
print(company[-1])
#index 10 of the string
print(company[10])
#creating acronym for string
acronym1="PFE"
acronym2="CFA"
#using index to determine the position of letter in string
company="Coding For All"
print(company.index("C"))
print(company.index("F"))
company+="people"
#using rfind to determine the position of letter in string
print(company.rfind("l"))
#using index or find to determine the position of first occurrence of world in string
company="You cannot end a sentence with because because because is a conjunction"
print(company.index("because"))
print(company.find("because"))
#using rindex or rfind to determine the position of last occurrence of world in string
print(company.rindex("because"))
print(company.rfind("because"))
#using strip to remove whitespace from the beginning and end of string
print(company.strip("because because because"))
#checking if the string starts with a certain word
company="Coding For All"
print(company.startswith("Coding"))
company="Coding For All"
print(company.startswith("coding"))
#removing whitespace from the beginning and end of string
company="   Coding For All      "
print(company.strip())
#which of the following variables return true when we use isidentifier() method
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier()) #the second variable is a valid identifier because it starts with a letter and contains only letters, numbers, and underscores. The first variable is not a valid identifier because it starts with a number.
#joining a list of strings into a single string using hash with space string.
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libraries))
# printing a sentence
print("I am enjoying this challenge.\nI just wonder what is next.")
#using escape sequence to print a sentence
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t25\tFinland\tHelsinki")
#Use the string formatting method to display
radius=10
area=3.14*radius**2
print("radius=" + str(radius))
print("area=" + str(area))
print("The area of a circle with radius " + str(radius) + " is " + str(area) + " meters square.")
#using string formatting method to display
print("8 + 6 = " + str(8+6))
print("8 - 6 = " + str(8-6))
print("8 * 6 = " + str(8*6))
print("8 / 6 = " + str(8/6))
print("8 % 6 = " + str(8%6))
print("8 // 6 = " + str(8//6))
print("8 ** 6 = " + str(8**6))