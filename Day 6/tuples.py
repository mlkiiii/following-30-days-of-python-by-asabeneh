#empty tuple
empty_tuple=()
#tuple of my siblings
brothers=("moemen","mahdi")
sisters=("salma","hlima")
#joining the two tuples
siblings=brothers+sisters
#number of siblings
print("Number of siblings: ", len(siblings))
#adding father and mother to tuple
father_and_mother=("Fathi","ichrak")
family_members=siblings+father_and_mother
print(family_members)
#unpacking parents
parents=family_members[-2:]
#food stuff
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals=("dog","cat","snake")
food_stuff_tp=fruits+vegetables+animals
print(food_stuff_tp)
#chhanging the tuple to list
food_stuff_lt=list(food_stuff_tp)
#slicing the middle item or items from food_stuff_lt list
if len(food_stuff_lt)%2==0:
    print(food_stuff_lt[len(food_stuff_lt)//2])
    print(food_stuff_lt[len(food_stuff_lt)//2 -1])
else:
    print(food_stuff_lt[len(food_stuff_lt)//2])
#slicing out the first and last 3 items
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
#deleting the tuple
del(food_stuff_tp)
#Checking if an item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia is in the nordic countries: ","Estonia" in nordic_countries)
print("Iceland is in the nordic countries: ","Iceland" in nordic_countries)
