
# Sum of multiples of 3 or 5 below a given number
# e.g: sum of multiples below 10 (3, 5, 6, 9) = 23

multiple_list = []

# Receive user input
while True:
	try:
		number = int(input("Please input a number"))
	except ValueError:
		pass
	else:
		break

# Iterate through numbers, checking for multiples
for num in range(0, number, 3):
	if (not number in multiple_list):
 		multiple_list.append(num)

for num in range(0, number, 5):
	if (not number in multiple_list):
 		multiple_list.append(num)

# Present calculations
print("The sum of all multiples of 3 and 5 below", number, "=", sum(multiple_list))