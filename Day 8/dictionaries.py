#creating an empty dictionary
dog=dict()
#adding keys and values to the dict
dog['name']='bob'
dog['color']='black'
dog['breed']='malinois'
dog['legs']='4'
dog['age']=7
#creating a student dictionary
student=dict()
student['first_name']="mohamed"
student['last_name']="malki"
student['gender']="male"
student['age']=19
student['marital_status']="single"
student['skills']=["python","it"]
student['country']="tunisia"
student['city']="ban arous"
student['address']="64 street"
#getting the length of the student dictionary
len(student)
#getting the skills and checking their data type
print(student['skills'])
print(type(student['skills']))
#adding values to skills
student['skills'].update("eating","playing basketball")
#getting keys as list
student.keys()
#getting values as list
student.values()
#changing the dict to a list of tuples
student_1=student.items()
#deleting one item from one of the dicts
student.popitem()
#deleting one of the dictionaries
del dog