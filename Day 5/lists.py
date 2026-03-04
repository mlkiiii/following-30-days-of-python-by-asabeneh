#declaring an empty list
list=[]
#declaring list with items
list=[1,2,3,4,5]
#length of list
print(len(list))
#accessing list items
print(list[0])
print(list[3])
print(list[-1])
#mixed data types in list
mixed_data_types=["mohamed",20,78,"engineer","Tunisia"]
#declaring a list of companies
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#printing the list of companies
print(it_companies)
#printing the number of companies
print(len(it_companies))
#printing first,middle,and last company in the list 
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])
#printing the list of companies after modifying one of the companies
it_companies[0]="Meta"
print(it_companies)
#adding an item to the list 
it_companies.append("Facebook")
print(it_companies)
#changing one off the items to Uppercase
it_companies[5]=it_companies[(5)].upper()
#joining the list with a string '#'
print('# '.join(it_companies))
#checking if a certain company exists in the list
print("Facebook" in it_companies)
#sorting the list
it_companies.sort()
#reversing the list
it_companies.reverse()
#slicing the list to get the first three companies 
print(it_companies[0:3])
#slicing the list to get the last three companies
print(it_companies[-3:])
#slicing out the middle company or companies
print(it_companies[len(it_companies)//2])
#removing the first it commpany from the list 
it_companies.remove(it_companies[0])
#removing the middle it company from the list 
it_companies.remove(it_companies[len(it_companies)//2])
#removing the last it company from the list
it_companies.remove(it_companies[-1])
#destroying the list
it_companies.clear()
#joining 2 lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
#copying the joined list to a variable full_stack
full_stack=front_end.copy()
#sorting the list and finding the max and min 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Max age:", ages[-1])
print("Min age:", ages[0])
#adding the min age and max age to the list again 
ages.append(ages[0])
ages.append(ages[-1])
#finding the median age
ages.sort()
n = len(ages)
if n % 2 != 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Median age:", median)
#finding the average age 
print("Average age:", sum(ages)/len(ages))
#finding the range of the ages
print("Range of ages:", ages[-1] - ages[0])
#comparing the value of (min age - average age) and (max age - average age)
print("Min age - Average age:", ages[0] - (sum(ages)/len(ages)))
print("Max age - Average age:", ages[-1] - (sum(ages)/len(ages)))

