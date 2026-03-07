#Iterating 0 to 10 using for loop, do the same using while loop
for i in range(11):
    print(i)
#Iterating 10 to 0 using for loop, do the same using while loop
for i in range(10,-1,-1):
    print(i)
#Writing a loop that makes seven calls to print(), so we get on the output the following triangle:
hash_message='#'
for i in range(7):
    print(hash_message)
    hash_message +='#'
#using nested loops to create a block of hashtags
hash_message='#'
for i in range(7):
    hash_message='#'
    for i in range(7):
        hash_message +=" " +'#'
    print(hash_message)
#printing a specified pattern from the repo day 10 loops exercise 1 question n°5
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
for i in range(11):
    print(str(i)+" "+"x"+" "+str(i)+" "+"="+" "+str(i*i))
#printing list items using for loop
list= ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print (item)
#iterating from 0 to 100 and printing only the even numbers
for i in range(101):
    if i%2==0:
        print(i)
#iterating from 0 to 100 and printing only the odd numbers
for i in range(101):
    if i%2!=0:
        print(i)
#calculating the sum of all numbers from 0 to 100 using for loop
sum=0
for i in range(101):
    sum +=i
print("The sum of all numbers is "+str(sum)+".")
#calculating the sum of even numbers and odd numbers from 0 to 100 using for loop
sum_even=0
sum_odd=0
for i in range(101):
    if i%2==0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is " +str(sum_even)+". And the sum of all odds is "+str(sum_odd)+".")
#extracting all the countries that contain land in their names 
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',  'Tonga',  'Trinidad and Tobago',  'Tunisia',  'Turkey',  'Turkmenistan',  'Tuvalu',  'Uganda',  'Ukraine',  'United Arab Emirates',  'United Kingdom',  'United States',  'Uruguay',  'Uzbekistan',  'Vanuatu',  'Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
]
for country in countries:
    if 'land' in country:
        print(country)
#reversing a list
fruits=['banana', 'orange', 'mango', 'lemon']
reversed_list=list()
for i in range(len(fruits)-1,-1,-1):
    reversed_list.append(fruits[i])
print(reversed_list)
