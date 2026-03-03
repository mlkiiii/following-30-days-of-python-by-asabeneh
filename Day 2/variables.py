#Day2: 30 days of python programming
first_name="Mohamed"
last_name="Malki"
full_name=first_name+" "+last_name
country="Tunisia"
city="Ben Arous"
age=20
year=2026
is_married=False
is_true=True
is_light_on=True
full_name,country,age,is_married="Mohamed Malki","Tunisia",20,False
#variables types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
#length of my first name
print(len(first_name))
#comparing the length of first name and last name
print(len(first_name)==len(last_name))
#checking if the first name is greater than the last name
print(len(first_name)>len(last_name))
num_one=5
num_two=4
#total of number on + number two
total=num_one+num_two
print(total)
#difference of number one - number two
diff=num_one-num_two
print(diff)
#product of number one * number two
product=num_one*num_two
print(product)
#division of number one / number two
division=num_one/num_two
print(division)
#remainder of number one % number two
remainder=num_one%num_two
print(remainder)
#exponent of number one ** number two
exp=num_one**num_two
print(exp)
#floor division of number one // number two
floor_division=num_one//num_two
print(floor_division)
#area of a circle 
radius=30
pi=3.14
area_of_circle=pi*radius**2
print(area_of_circle)
#circumference of a circle
circumference_of_circle=2*pi*radius
print(circumference_of_circle)
#radius as an input from user
radius=float(input("enter the radius of the circle:"))
area_of_circle=pi*radius**2
print(area_of_circle)
#using input built-in function to store user information
first_name=input("enter your first name:")
last_name=input("enter your last name:")
country=input("enter your country:")
age=int(input("enter your age:"))
#run help function to check the list of keywords in python
help('keywords')