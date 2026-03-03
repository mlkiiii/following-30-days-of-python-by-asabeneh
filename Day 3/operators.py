age=int()
weight=float()
complex_number=complex()
#calculating area of triangle
base=float(input("Enter the base of triangle: "))
height=float(input("Enter the height of triangle: "))
area=0.5*base*height
print("Area of triangle is: ",area)
#calculating the perimeter
side_a=float(input("Enter the length of side a:"))
side_b=float(input("Enter the length of side b:"))
side_c=float(input("Enter the length of side c:"))
perimeter=side_a+side_b+side_c
print("Perimeter of triangle is : ",perimeter)
#calculating area and perimeter of rectangle
length=float(input("Enter the length of rectangle: "))
width=float(input("Enter the width of rectangle: "))
area_rectangle=length*width
perimeter_rectangle=2*(length+width)
print("Area of rectangle is: ",area_rectangle)
print("Perimeter of rectangle is: ",perimeter_rectangle)
#calculating area and circumference of circle
radius=float(input("Enter the radius of circle: "))
pi=3.14159
area=pi*radius**2
circumference=2*pi*radius
print("Area of the circle is: ",area)
print("Circumference of the circle is : ",circumference)
#calculate the slope of y=2x-2
m=2
b=-2
slope=m
y_intercept=(0,b)
x_intercept=(-b/m,0)
print("Slope of the line is: ",slope)
print("X-intercept of the line is: ",x_intercept)
print("Y-intercept of the line is: ",y_intercept)  
#calculating the slope between two points (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m=(y2 - y1) / (x2 - x1)
print("Slope between points (2,2) and (6,10) is: ",m)
print("Euclidean distance between points (2,2) and (6,10) is: ",((x2 - x1)**2 + (y2 - y1)**2)**0.5)
#comparing the slopes of the line y=2x-2 and the line passing through points (2,2) and (6,10)
print("slopes are equal: ", m == slope)
print("slope task 8 is greater than slope task 9: ", m < slope)
print("slope task 8 is less than slope task 9: ", m > slope)
#calculating the vallue of y of y=x**2 + 6x + 9 when y is 0
a=1
b=6
c=9
delta=b**2 - 4*a*c
if delta > 0:
    root1=(-b + delta**0.5) / (2*a)
    root2=(-b - delta**0.5) / (2*a)
    print("The roots are: ", root1, "and", root2)
elif delta == 0:
    root=-b / (2*a)
    print("The root is: ", root)
else:
    print("No real roots exist.")
#calculating the length of python string 'python' and comparing it with the length of string 'dragon' with a falsy statement
python_length=len("python")
dragon_length=len("dragon")
print("Length of 'python': ", python_length)
print("Length of 'dragon': ", dragon_length)
print("Are the lengths equal? ", python_length == dragon_length)
#checking if 'on' is found in both 'python' and 'dragon'
print("'on' in 'python': ", 'on' in "python")
print("'on' in 'dragon': ", 'on' in "dragon")
#checking if 'jargon' is found in the sentence
sentence="I hope this course is not full of jargon."
print("'jargon' in sentence: ", 'jargon' in sentence)
#finding the length of the next python and convert it into a float and then into a string 
