# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#finding thz length of it_companies
print(len(it_companies))
#adding twitter to the list 
it_companies.add("Twitter")
#inserting multiple it companies to it_companies
it_companies.update("Meta","Alpha")
#removing one company from it_companies
it_companies.remove("Facebook")
#the difference between remove and discard that remove it removes an element and if the element is not found it raises a keyerror but discard does nothing
#joining A and B
A.union(B)
#finding interactions between a and b 
A.intersection(B)
#finding if A subset b
A.issubset(B)
#checking if they are disjoints
A.isdisjoint(B)
#joining a with b and b with a 
A.union(B)
B.union(A)
#deleting sets
del A
del B
#converting list ages to set then comparing their lengths
len_age_list=len(age)
len_age_set=len(set(age))
print("list is longer than set: ",len_age_set > len_age_list)
print("set is longer than list: ",len_age_set < len_age_list)
print("list is longer than set: ",len_age_set == len_age_list)
#the difference between tuple list and set are:
#the list is mutable, ordered, allows duplicates, can be created with squares || mostly used for collections that need modifications, like dynamic arrays or queues
#the tuple is immutable,ordered,allows duplicates, can be created with sequences || mostly used for fixed collections of related data
#the set is mutable,unordered ,no duplicates,can be created with curly braces || mostly used for unique collections ,membership testing or mathematical set operations 
#last question in exercise 
#declaring the sequence 
sequence="I am a teacher and I love to inspire and teach people"
set_of_words=set(sequence.split(" "))
print (set_of_words)
