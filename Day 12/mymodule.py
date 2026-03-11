#creating a function that generates a six digits/characters id 
import string
from random import*
def random_user_id():
    all_characters=string.ascii_letters + string.digits
    length=len(all_characters)-1
    id=""
    for i in range (6):
        random_number=randint(0,length)
        id+=all_characters[random_number]
    print(id)
#creating a function that generates a six digits/characters id by user
def user_id_gen_by_user():
    number_of_ids=int(input("the number of ids: "))
    length_of_id=int(input("the length of ids: "))
    all_characters=string.ascii_letters + string.digits
    length=len(all_characters)-1
    for i in range (number_of_ids):
        id=""
        for j in range (length_of_id):
            random_number=randint(0,length)
            id+=all_characters[random_number]
        print(id)
#creating a function that generate an rgb color
def rgb_color_gen():
    n1=randint(0,255)
    n2=randint(0,255)
    n3=randint(0,255)
    return("rgb("+str(n1)+","+str(n2)+","+str(n3)+")")
#creating a function that generates a hexadecimal color
def list_of_hexa_colors(number):
    all_the_hexadecimals="abcdef123456789"
    list_of_colors=[]
    for i in range(number):
        color=""
        for i in range(6):
            index_of_chr=randint(0,len(all_the_hexadecimals)-1)
            color += all_the_hexadecimals[index_of_chr]
        list_of_colors.append("#"+color)
    return list_of_colors
#creating a function that returns a list of rgb colors
def list_of_rgb_colors(number):
    list_of_colors=[]
    for i in range(number):
        list_of_colors.append(rgb_color_gen())
    return list_of_colors
def generate_colors(type,number):
    if type.lower()=="hexa":
        return(list_of_hexa_colors(number))
    elif type.lower()=="rgb":
        return(list_of_rgb_colors(number))
    else:
        print("Type is indifined")
#a functionn that shuffles a list
def shuffle_list(listq):
    shuffled_items = listq[:]  
    shuffle(shuffled_items)  # Shuffle in place
    print(shuffled_items)
#a function which returns an array of seven random numbers in a range of 0-9.
def seven_numbers():
    array=[]
    while len(array)<7:
        number=randint(0,9)
        if not number in array:
            array.append(number)
    return array
