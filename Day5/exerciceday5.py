#1
first_list = []
#2
second_list = ["item1","item2", "item3", "item4", "item5"]
#3
print(len(second_list))
#4
first_item = second_list[0]
middle_item = second_list[2]
last_item = second_list[-1]
#5
mixed_data_types = ["Entamene", "21", "1.95", "Celibatary", "Aix-les-Bains"]
#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IMB", "Oracle", "Amazon"]
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[len(it_companies)%2 + 2])
print(it_companies[-1])
#10
first_companies = it_companies[0] = "Antrophic"
print(it_companies)
#11
it_companies.append("Nvidia")
print(it_companies)
#12
it_companies.insert(7, "OpenIa")
print(it_companies)
#13
upper = it_companies[0].upper()
it_companies[0] = upper
print(it_companies)
#14
it_companies.append("# ")
print(it_companies)
#15
check_list = "Microsoft" in it_companies
print(check_list)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
first_companies = it_companies[3:]
print(first_companies)
#19
last_companies = it_companies[:-3]
print(last_companies)
#20
middle_companies = it_companies[0:4] + it_companies[6:len(it_companies)]
print(middle_companies)
#21
it_companies.pop(0)
print(it_companies)
#22
it_companies.pop(int(len(it_companies)/2))
print(it_companies)
#23
it_companies.pop(-1)
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

#27
full_stack = ["Python", "SQL"]
front_end.extend(full_stack)
print(front_end)

#EXERCICE 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print("Le minimun de la liste est : ", ages[0])
print("Le Maximun de la liste est :", ages[-1])

ages.append(ages[0])
ages.append(ages[-1])

ages.sort()

median_of_list = int(len(ages)/2)
print("La médiane de la liste est : ", ages[median_of_list])

first, second, third, four, five, six, seven, eight, nine, ten, eleven, twelves = ages

sum_of_list = first + second + third + four + five + six + seven + eight + nine + ten + eleven 
average = int(sum_of_list / len(ages))
print(average)

range_list = ages[-1] - ages[0]
print(range_list)

value_first = abs(ages[0] - average)
value_second = abs(ages[-1] - average)

print("La valeur absolue de min - moyenne >= la valeur absolue de max - moyenne", value_first >= value_second )
