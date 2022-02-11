import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
selected_letters = random.sample(letters, nr_letters)  # seleciona randomicamenbte as letras
selected_numbers = random.sample(numbers, nr_numbers)  # seleciona randomicamente os numeros
selected_symbols = random.sample(symbols, nr_symbols)  # seleciona randomicamente os simbolos
final_list = selected_symbols + selected_letters + selected_numbers  # cria uma unica lista
random.shuffle(final_list)  # randomiza a lista
password = ''.join(str(x) for x in final_list)  #transforma a lista em uma string
print('Here is your password: {}'.format(password))
