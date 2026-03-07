#checking if a person can drive a car or no 
age=int(input("Enter your age: "))
if age>=18:
    print("you're old enough to drive")
else:
    print("You need "+str(18-age) +"more years to learn to drive")
#comparing to ages
my_age=19
your_age=int(input("Enter your age: "))
if my_age>your_age:
    if my_age-your_age==1:
        print("i'm 1 year older than you")
    else:
        print("i'm "+str(my_age-your_age) +" years older than you")
elif your_age>my_age:
    if your_age-my_age==1:
        print("You're 1 year older than you")
    else:
        print("You're "+str(your_age-my_age) +" years older than you")
else:
    print("We are equal")
#comparing two numbers
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
if a>b:
    print(str(a)+ " is greater than" +str(b))
elif a<b:
    print(str(a)+ " is smaller than" +str(b))
else:
    print(str(a)+ " is equal to " +str(b))
#writing a code that give grades to student based on their scores
score=int(input("Enter your score"))
if 0<score<59:
    grade="F"
elif 60<score<69:
    grade="D"
elif 70<score<79:
    grade="C"
elif 80<score<89:
    grade="B"
elif 90<score<100:
    grade="A"
else:
    print("score is wrong")
print(grade)
#checking the season by getting the month as an input from user
autumn=["September", "October" , "November"]
winter=["December", "January" , "February"]
spring=["March", "April", "May"]
summer=["June", "July" , "August"]
month=input("Enter the month: ")
if month in autumn:
    print("The season in Autumn")
elif month in winter:
    print("The season in Winter")
elif month in spring:
    print("The season in Spring")
elif month in summer:
    print("The season in Summer")
else:
    print("The month is incorrect")
#the fruit list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("Enter the fruit: ").lower()
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)
#Exercise n°3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React',"MongoDB", 'Node', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Checking if the person dictionary has skills key, if so printing out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
#Checking if the person dictionary has skills key, if so checking if the person has 'Python' skill and printing out the result.
if 'skills' in person:
    print('python' in person['skills'])
#If a person skills has only JavaScript and React, printing('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, printing('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Printing('He is a fullstack developer'),
# else printing('unknown title') - for more accurate results more conditions can be nested!
if ("React" and "Node" and "MongoDB") in person['skills']:
    print('He is a fullstack developer')
elif ("JavaScript" and "React") in person['skills']  and len(person['skills'])==2:
    print('He is a front end developer')
elif ("Node" and "Python" and "MongoDB") in person['skills']:
    print('He is a backend developer')
else:
    print('unknown title')
#If the person is married and if he lives in Finland, printing the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] and person['country']:
    print(person["first_name"] +" "+ person["last_name"] +" "+"Lives in Finland. He is Married")