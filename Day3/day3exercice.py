import math

#1 
age = 21
#2
height = 1.95
#3
complex_number = 2 + 2j

#4

height_of_triangle = input("What's the height of the triangle ? ")
base_of_triangle = input("What's the base of the triangle ? ")

height_of_triangle = float(height_of_triangle)
base_of_triangle= float(base_of_triangle)

area_of_triangle = 0.5 * base_of_triangle * height_of_triangle

print("The area of ur triangle = ", area_of_triangle)

#5

side_a =  float(input("Enter the side a : "))
side_b = float(input("Enter the side b : "))
side_c = float(input("Enter the side c : "))

perimeter_of_triangle = side_a + side_b + side_c 

print("The perimeter of a triangle is:", perimeter_of_triangle)

#6

length_rectangle = float(input("Enter the length :"))
wide_rectangle = float(input("Enter the wide :"))

area_of_rectangle = wide_rectangle * length_rectangle
perimeter_of_rectangle = 2 * (wide_rectangle + length_rectangle)

print("The area of the rectangle is : ", area_of_rectangle ,"and the perimeter of the rectangle is :", perimeter_of_rectangle)

#7

radius_circle = float(input("Enter the radius of the circle :"))

area_of_circle = math.pi * (radius_circle ** 2)
circumference_of_circle = math.pi * 2 * radius_circle

print("The area of the circle:", area_of_circle, "and the circumference is:", circumference_of_circle)

#8
m = 2
b_slope= -2

slope = m 
y_intercept = m*0 + b_slope
x_intercept = - b_slope / m 

print("slope = ", slope, ",y intercept = ", y_intercept, " and x intercept =", x_intercept)

#9

x1 = 2 
y1 = 2 
x2 = 6
y2 = 10

slope_pythagore = (y2-y1)/(x2-x1)
euclidian_distance = (((x1-y1)**2) + ((x2-y2)**2) )** 0.5

#10

print(slope == slope_pythagore)
print(slope > slope_pythagore)
print(slope < slope_pythagore)

number_x = int(input("Choose a number to resolve the next equation : x^2 + 6x + 9 "))

#11

equation = number_x **2 + 6 * number_x + 9 

print(equation)

#12

word_python = "python"
word_dragon = "dragon"

len_python = len(word_python)
len_dragon = len(word_dragon)

print(len_dragon < len_python)

#13

on_comparator = "on"

print(on_comparator in word_python and word_dragon)

#14

sentence_jargon = "i hope this course is not full of jargon"
jargon = "jargon"
print("in is it in this sentence ? I hope this course is not full of jargon", jargon in sentence_jargon)

#15

print("There is no 'on' in dragon and python", on_comparator not in word_python and word_python)

#16

float_len_python = float(len_python)
string_len_python = str(float_len_python)

#17
number_choosen = float(input("Choose a number: "))
print(number_choosen % 2 == 0)

#18

floor_division_eighteen = 7//3

print("The floor division of 7 by 3 is equal to 2.7: ", floor_division_eighteen == int(2.7))

#19

print ("Type of '10' is equal to type of 10 ? ", type("10") == type(10))

#20

print("The type of '9.8' is equal to 10 ?", type(int(float("9.8")))== type(10) )

#21

hours_of_work = int(input("Enter ur hours of work:" ))
rate_per_hour = int(input("Enter ur rate per hour: "))

salary = rate_per_hour * hours_of_work

print("Ur weekly salary is: ", salary)

#22

years_lived = int(input("Enter numbers of year u lived: "))

second_lived = 31536000 * years_lived

print("You haved lived ", second_lived, "seconds.")

#23

print("1\t1\t1\t1\t1")
print("2\t1\t2\t4\t8")
print("3\t1\t3\t9\t27")
print("4\t1\t4\t16\t64")
print("5\t1\t5\t25\t125")


print(1,1,1,1**2,1**2)
print(2,1,2,2**2,2**3)
print(3,1,3,3**2,3**3)
print(4,1,4,4**2,4**3)
print(5,1,5,5**2,5**3)

