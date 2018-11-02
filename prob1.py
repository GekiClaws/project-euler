
# Sum of multiples of 3 or 5 below a given number
# e.g: sum of multiples below 10 (3, 5, 6, 9) = 23

multiples_3 = []
multiples_5 = []

# Receive/validate user input
while True:
	try:
		number = int(input("Please input a number"))
	except ValueError:
		pass
	else:
		break

# Iterate through multiples and append to lists
for num in range(0, number, 3):
	multiples_3.append(num)

for num in range(0, number, 5):
	multiples_5.append(num) 		

multiples_5 = list(set(multiples_5) - set(multiples_3))

result = multiples_3+multiples_5

# Present calculations
print("The sum of all multiples of 3 and 5 below", number, "=", sum(result))