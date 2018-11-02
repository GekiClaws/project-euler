
# Smallest positive number that is evenly
# divisible by all of the numbers
# from 1 to input number

# Receive/validate user input
while True:
	try:
		number = int(input("Please input a number"))
	except ValueError:
		pass
	else:
		break

# Prime number algorithim
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def ispower(number):
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

	return prime_factors

# Data processing
the_number = 1

for num in range(1, number+1):
	if isprime(num): # operation for prime number
		the_number *= num
	elif len(list((ispower(num).keys()))) == 1:
		the_number *= int(list(ispower(num).keys())[0])
	else:
		pass

print(the_number)
