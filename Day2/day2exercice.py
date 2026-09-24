import math 

#Exercice 1 


first_name = "Louai"
last_name = "Entamene"
full_name = first_name + last_name 
country = "France"
age = 21
year = 2026
is_married = False
is_True = True 
is_Light_on = True 

name_of_pet,number_of_brother, city = "Joe", "Ilyes & Iskandar", "Grenoble"

#Exercice 2 

type(first_name)
type(last_name)
type(full_name)
type(country)
type(age)
type(year)
type(is_married)
type(is_True)
type(is_Light_on)
type(name_of_pet)
type(number_of_brother)
type(city)

len_fisrt_name = len(first_name)
len_last_name = len(last_name)

num_one = 5 
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one % num_two
remainder = num_two / num_one
exp = num_one ** num_two
floor_division = num_one // num_two


radius = 30 
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

radius_user = input("Write ur radius")

area_of_circle_user = math.pi * radius_user ** 2

print(area_of_circle_user)

last_name_user = input("What's ur last name ? ")
first_name_user = input("What's ur first name ? ")
age_user = input("What's ur age ? ")
country_user = input("What's ur country ? ")

