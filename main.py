import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
		   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
		   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters would you like in your password?\n "))
num_numbers = int(input("How many numbers would you like?\n "))
num_symbols = int(input("How many symbols would you like?\n "))

# Password Generator using random.sample()

# rand_letters = random.sample(letters, num_letters)
# rand_numbers = random.sample(numbers, num_numbers)
# rand_symbols = random.sample(symbols, num_symbols)
#
# password = rand_letters + rand_numbers + rand_symbols
# random.shuffle(password)
#
# password = ''.join(password)

# Password generator with for loop

password = ""

for char in range(1, num_letters + 1):
	rand_letters = random.choice(letters)
	password += rand_letters

for num in range(1, num_symbols + 1):
	rand_numbers = random.choice(numbers)
	password += rand_numbers

for symbol in range(1, num_symbols + 1):
	rand_symbols = random.choice(symbols)
	password += rand_symbols

password_list = list(password)
random.shuffle(password_list)

password = ''.join(password_list)

print(password)
