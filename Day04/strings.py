# Exercises - Day 4

#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'

challenge = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4

print(challenge)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
string1 = 'Coding'
string2 = 'For'
string3 = 'All'
concat_string = string1 + ' ' + string2 + ' ' + string3
print(concat_string)

#3. Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding For All'

#4.
print(company)

#5.
print(len(company))

#6.
print(company.upper())

#7.
print(company.lower())

#8.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9.
print(company[7:])

#10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print(company.index("Coding"))
print("Coding" in company)

#11.
print(company.replace('Coding', 'Python'))

#12.
sentence = "Python For Everyone"
print(sentence.replace('Everyone', 'All'))

#13.
print(company.split())

#14.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

#15
print(company[0])

#16.
print(len(company) -1)

#17.
print(company[10])

#18.
words = sentence.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

#19.
word = company.split()
abbreviation = word[0][0] + word[1][0] + word[2][0]
print(abbreviation)

#20.
print(company.index("C"))

#21.
print(company.index("F"))

#22.
text = "Coding For All People"
print(text.rfind("I"))

#23.
text2 = "You cannot end a sentence with because because because is a conjunction"
print(text2.find("because"))

#24.
print(text2.rindex("because"))

#25.
print(text2[31:55])

#26.
print(text2.find("because"))

#27.
print(text2[31:55])

#28.
print(company.startswith("Coding"))

#29.
print(company.endswith("coding"))

#30.
text3 = '   Coding For All      '
print(text3.strip())

#31.
text4 = '30DaysOfPython'
text5 = 'thirty_days_of_python'
print(text4.isidentifier())
print(text5.isidentifier())

#32.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

#33.
print("I am enjoying this challenge \nI just wonder what is next")

#34.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius {} is {:.2f} meters square.'.format(radius, area)
print(formated_string)

#36.
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')