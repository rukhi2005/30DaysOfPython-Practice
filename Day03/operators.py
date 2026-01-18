# #Exercises - Day 3
#1
age = 20 

#2
my_height = 4.98 

#3
complex_number = 1 + 1j

#4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_the_triangle = 0.5 * base * height
print(area_of_the_triangle)

#5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_the_triangle = side_a + side_b + side_c
print(perimeter_of_the_triangle)

#6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_of_the_rectangle = length * width
perimeter_of_the_rectangle = 2 * (length + width)
print("The area is: ", area_of_the_rectangle)
print("The perimeter is: ", perimeter_of_the_rectangle)

#7
radius_of_circle = float(input("Enter radius: "))
pi = 3.14
area_of_circle = pi * radius_of_circle * radius_of_circle
circumference_of_circle = 2 * pi * radius_of_circle
print("area: ", area_of_circle)
print("circumference: ", circumference_of_circle)

#8
m = 2
b = -2

print("Slope: ", m)
print("Y-intercept: ", b)

# x-intercept formula: x = -b / m
x_intercept = -b / m
print("X-intercept:", x_intercept)

#9
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Slope =", slope)
print("Distance =", distance)

#10
slope1 = 2
slope2 = (10 - 2) / (6 - 2)
print(slope1 == slope2)

#11
x = -3
y = x*x + 6*x + 9
print(y)
print("The y was 0 at x = ", x)

#12
print(len("python") > len("dragon"))

#13
print('on' in 'python' and 'on' in 'dragon')

#14
print('jargon' in 'I hope this course is not full of jargon')

#15
print(not ('on' in 'python' and 'on' in 'dragon'))

#16
text = len("python")
print(float(text))
print(str(text))

#17
num = int(input("Enter your number: "))
even = num % 2 == 0
print(even)

#18
print(7 // 3 == int(2.7))

#19
print(type('10') == type(10))

#20
print(int(float('9.8')) == 10)

#21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is ", weekly_earning)

#22
years = int(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60
print("You can live for", seconds, "seconds.")

#23
print(1, 1, 1, 1*1, 1*1*1)
print(2, 1, 2, 2*2, 2*2*2)
print(3, 1, 3, 3*3, 3*3*3)
print(4, 1, 4, 4*4, 4*4*4)
print(5, 1, 5, 5*5, 5*5*5)


