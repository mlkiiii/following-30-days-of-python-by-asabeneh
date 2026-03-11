#filtering only negative and zero in the list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers=[i for i in numbers if i<1]
print(filtered_numbers)
#fattening a list of listss
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list=[j for i in list_of_lists for j in i ]
print(list)
#creating a list of tuples
list=[(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print (list)
#fattening a list of listss
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list=[[l[0].upper(),l[0][:3].upper(),l[1].upper()] for i in countries for l in i]
print(flattened_list)
#changing to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dicto=[{'country': l[0].upper(), 'city': l[1].upper()} for i in countries for l in i]
print(dicto)
#changing a list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name=[l[0]+" "+l[1] for i in names for l in i]
print(full_name)
#a lambada function to resolve a slope 
slope=lambda y2,y1,x2,x1:(y2-y1)/(x2-x1) 
print(slope(12,2,8,4))