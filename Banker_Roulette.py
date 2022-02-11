import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_pleope = len(names)  # numero de pessoas na lista
number_choise = random.randint(0, number_of_pleope-1)  # escolhe o numero (posicao da lista) aleatorio na lista
pay_bay_people = names[number_choise]   # pega a pessoa escolhida aleatoria para imprimir
print('{} is going to buy the meal today!'.format(pay_bay_people))
