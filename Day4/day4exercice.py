#1 
space = " "
thirty_word = "Thirty"
days_word = "days"
of_word = "of"
python_word = "Python"

sentence_introduction = thirty_word + space + days_word + space + of_word + space + python_word     
print(sentence_introduction)

#2
coding_word = "Coding"
for_word = "for"
all_word = "all"

coding_sentence = coding_word + space + for_word + space + all_word
print(coding_sentence)

#3
company = coding_sentence
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
coding_slice = company[0:6]
print(coding_slice)
#10
print(company.find("Coding"))
#11
rest_of_sentence = company[6:13]
python_company = python_word + rest_of_sentence
print(python_company)
#12
python_everyone = "Python for everyone"
print(python_everyone.replace("for everyone", "for all"))
#13
print(coding_sentence.split(" "))
#14
gafa_name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(gafa_name.split(", "))
#15
#The character at the index 0 in "Coding for All" == "C"
#16
#the last index in "Coding for All" is = len("Coding for All")- 1 = 13
#17
#The character at the index 10 is " ".
#18
abreviation_p = python_company[0]
abreviation_f = company[7]
abreviation_a = company[11]

abreviation_python = abreviation_p + abreviation_f +abreviation_a

print(abreviation_python)
#19
abreviation_c = company[0]
abreviation_company = abreviation_c + abreviation_f + abreviation_a
print(abreviation_company)
#20
print(company.find("C"))
#21
print(company.find("f"))
#22
print(company.rfind("l"))
#23
long_sentence = " You cannot end a sentence with because because because is a conjunction"
print(long_sentence.find("because"))
#24
print(long_sentence.rfind("becasue"))
#25
word = "because"
start = long_sentence.find(word)
end = long_sentence.rfind(word) + len(word)

print(long_sentence[start:end])

#26 = #24
#27 = #25

#28
print(company.startswith("Coding"))
#29
print(company.endswith("Coding"))
#30
sentence_with_space = '   Coding For All      ' 
print(sentence_with_space.strip())
#31
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
# it will be true for the second one bc isdentifier verify is a string is full of character
# and the first one start with numbers
#32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))

#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name \tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki ")
#35
print("radius = 10 ")
print("area = 3.14 ** radius ** 2")
print("The area of the circle with a 10 radius is 314 meters square")
#36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")