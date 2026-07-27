countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#map() = "Change everyone."
#filter() = "Keep only the good ones."
#() = "Turn many into one."
#Higher-Order Function = "A function that works with other functions."
#Closure = "A function that carries its old variables in a backpack."
#Decorator = "A gift wrapper that upgrades a function with extra features."
def square(x):
    return x*x
def upper(name):
    return name.upper()
def length(var):
    if len(var)>4:
        return True
    else:
        return False
for country in countries:
    print(country)    
for name in names:
    print(name)
for number in numbers:
    print (number)
#LEVEL 2 EXERCICES 
uppered_countries=map(upper,countries)
print(list(uppered_countries))
squared_numbers=map(square,numbers)
print(list(squared_numbers))
uppered_names=map(upper,names)
print(list(uppered_names))
def check_land(var):
    if 'land' in var:
        return True
    else:
        return False
filtered_countries=filter(check_land,countries)
print(list(filtered_countries))
def length(var):
    if len(var)==6:
        return True
    else:
        return False
filtered_countries=filter(length,countries)
print(list(filtered_countries))
def check_six_chars(var):
    if len(var)>=6:
        return True
    else:
        return False
filtered_countries=filter(check_six_chars,countries)
print(list(filtered_countries))
def check_land(var):
    if 'E' in (var[0]).upper():
        return True
    else:
        return False
filtered_countries=filter(check_land,countries)
print(list(filtered_countries))
from functools import*
result=reduce(lambda x,y:x+','+y,filter(lambda x:len(x)>5,map(lambda x:x.upper(),countries+names)))
print(list(result))
def get_string_lists(list):
    string_list=[]
    for i in list:
        if type(i)==str:
            string_list.append(i)
    return string_list
sum=reduce(lambda x,y:x+y,numbers)
print(sum)
cocatenate=reduce(lambda x,y:x+','+y,countries)+"are north European countries"
print (cocatenate)
