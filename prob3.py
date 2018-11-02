
# Largest prime factor of a number
import math

# Receive/validate user input
while True:
	try:
		number = int(input("Please input a number"))
	except ValueError:
		pass
	else:
		break

prime_factors = {}
start_number = number

# Count number of 2s in number
if number%2==0:
	prime_factors["2"] = 0
	while (number%2==0):
		prime_factors["2"] += 1
		number /= 2 


# Limit number of calculations for speed
# - calculations for large numbers may be inaccurate 
if number < 100000000:
	range_num = start_number
else:
	range_num = int(math.sqrt(start_number))

# Count number of other prime factors in number
# Number must be odd by this point
for num in range(3, range_num, 2):
	if number%num==0:
		prime_factors[str(num)] = 0
		while (number%num==0):
			prime_factors[str(num)] += 1
			number /= num 

# If number is prime, add number to factor list for analysis later
if len(prime_factors) == 0:
	prime_factors[str(start_number)] = 1

# Analysis of factors
if len(prime_factors) == 1 and list(prime_factors.values())==[1] and list(prime_factors.keys()) != ['1']:
	print(start_number, "is prime, largest prime factor is", start_number)
else:
	print(start_number, "is not prime, largest prime factor is", list(prime_factors.keys())[-1])
