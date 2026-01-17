#Day 2: 30 Days of python programming
#Exercises: Level 1
first_name = 'Rukhaiya'
last_name = 'Mohammed'
full_name = first_name + " " + last_name
country = 'US'
city = 'San Jose'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
month, date = 'January', 17

#Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(month))
print(type(date))

print(first_name, len(first_name))

print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_two * num_one
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

r = 30
pi = 3.14
area_of_circle = pi * r * r
print(r)

circumference = 2 * pi * r
print(circumference)

radius = float(input("Enter the radius of the circle: "))
area = pi * radius * radius
print(area)

firstname = str(input("Enter your first name : "))
lastname = str(input("Enter your last name : "))
country = str(input("Enter your country : "))
age = int(input("Enter your age : "))

print(firstname)
print(lastname)
print(country)
print(age)

help('keywords')