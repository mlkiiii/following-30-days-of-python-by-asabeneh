#declaring a function add_two_numbers
def sum(a,b):
    return(a+b)
#function that calculates area of circle
def area_of_circle(r):
    area=r*r*3.14
    return area 
#writing a function of sum
def sum_all_numbers(*nums):
    for i in nums:
        if not (isinstance(i,(int,float))):
            return("The numbers contain other than int or float data type")
    sum=0
    for i in nums:
        sum +=i
    return sum
#converting a temperature from °C to °F:
def convert_c_to_f(temp_c):
    temp_f=(temp_c*(9/5))+32
    return temp_f
#checking a season by month
def check_season(month):
    autumn=["September", "October" , "November"]
    winter=["December", "January" , "February"]
    spring=["March", "April", "May"]
    summer=["June", "July" , "August"]
    month=input("Enter the month: ")
    if month in autumn:
        return("The season in Autumn")
    elif month in winter:
        return("The season in Winter")
    elif month in spring:
        return("The season in Spring")
    elif month in summer:
        return("The season in Summer")
    else:
        return("The month is incorrect")
#writing a function to calculate the slope of linear equation
def calculate_slope(x1,y1,x2,y2):
    if not all(isinstance(x1,x2,y1,y2),int,float):
        return("indexes are wrong")
    elif x1==x2 and y1==y2:
        return("This is a vertical line")
    return(y2-y1)/(x2-x1)
#a function that solve quadratic equation 
import math
def solve_quadratic_eqn(a,b,c):
    if a==0:
        return("a shouldn't be 0")
    det=(b*b)-4*a*c
    if det==0:
        return((-b)/(2*a))
    elif det<0:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-det) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return f"Two complex roots: {root1}, {root2}"
    else:
        root1 = (-b + math.sqrt(det)) / (2*a)
        root2 = (-b - math.sqrt(det)) / (2*a)
        return f"Two distinct real roots: {root1}, {root2}"
#a function that print full list element by element
def print_list(list):
    for element in list:
        print(element)
#a function that reversed an array
def reverse_list(array):
    reversed_array=[]
    for i in range(len(array)-1,-1,-1):
        reversed_array.append(array[i])
    return reversed_array
#a function that capitalize a list
def capitalize_list_items(list):
    for i in range(len(list)):
        list[i]=(list[i]).capitalize()
    return list 
#a function that add an item to a list
def add_item(list,item):
    list.append(item)
    return list
#a function that remove an item from a list
def remove_item(list,item):
    list.remove(item)
    return list
#a function that give the sum of all numbers in the range of a given number
def sum_of_numbers(number):
    sum=0
    for i in range(number+1):
        sum+=i
    return sum
#a function that give the sum of all odd numbers in the range of a given number
def sum_of_odd_numbers(number):
    sum=0
    for i in range(number+1):
        if i%2!=0:
            sum+=i
    return sum
#a function that give the sum of all even numbers in the range of a given number
def sum_of_even_numbers(number):
    sum=0
    for i in range(number+1):
        if i%2==0:
            sum+=i
    return sum
#a function that give the number of all even and odd numbers in the range of a given number
def even_and_odd(number):
    num_odd=0
    num_even=0
    for i in range(number+1):
        if i%2!=0:
            num_odd+=1
        else:
            num_even+=1
    return ("The number of odds are "+str(num_odd)+" \nThe number of evens are "+str(num_even))
#factoriel function
def factoriel(num):
    fact=1
    for i in range(num,0,-1):
        fact*=i
    return fact
#function that check if an item is empty or not
def is_empty(item):
    if item=="":
        return True
    else:
        return False
#different fnctions of list
#calculating the mean of a list
def calculate_mean(list):
    sum=0
    for item in list:
        sum+=item
    return sum/len(list)
#clculating the median of a list
def calculate_median(list):
    list.sort()
    if len(list)%2!=0:
        return("The median is "+str(list[len(list)//2]))
    else:
        return("The median is "+str(list[len(list)//2])+" "+str(list[(len(list)//2)-1]))
#calculating the mose of a list
from collections import Counter
def calculate_mode(list):
    counts = Counter(list)
    max_count = max(counts.values())
    if max_count==1:
        return[]
    else:
        return [item for item,num in counts.items() if num==max_count] 
#calculating the range of a list
def calculate_range(list):
    return(max(list)-min(list))
#calculating the variance of a list
def calculate_variance(list,sample=False):
    n=len(list)
    mean=calculate_mean(list)
    squared_diffs=[(x-mean)**2 for x in list]
    denominator=n-1 if sample else n
    sum=0
    for number in squared_diffs:
        sum+=number 
    varriance=sum/denominator
    return varriance
numbers = [6, 7, 3, 9, 10, 15]
#calculating the standard deviation of a list
def calculate_std(list):
    std=calculate_variance(list)**0.5
    return std
print(calculate_std([10, 12, 23, 23, 16, 23, 21, 16]))
#greeting function
def greet(name):
    if name=="":
        return("Hello, Guest!")
    else:
        return("Hello, "+name+"!")
#Creating a function called show_args to take an arbitrary number of named arguments and print their names and values
def show_args(**args):
    for key,value in args.items():
        print(key+":"+str(value))
#a function that checks if a a number is prime or no 
def is_prime(num):
    i=2
    if num==2 or num==1:
        return True
    while i<=num//2:
        if num%i==0:
            return False
        i+=1
    return True
#a functions that checks if all the items of the list are unique
def unique(list):
    dict=set(list)
    return len(dict)==len(list)
#checking if all the items of a list have the same data types
def check_data_type(list):
    data_type=type(list[0])
    for item in list:
        if data_type!=type(item):
            return False
    return True
#a function that check if the provided variable is a valid python variable
def valid_type(x):
    if (type(x) is str or type(x) is int or 
     type(x) is float or type(x) is dict 
     or type(x) is set or type(x) is list):
         return True
    else:
         return False