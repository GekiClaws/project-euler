
# Sum of even-valued Fibonacci terms below a number

# Receive/validate user input
while True:
	try:
		number = int(input("Please input a number"))
	except ValueError:
		pass
	else:
		break

# Generate Fibonacci sequence
fib_numbers = [1, 2]
while (fib_numbers[-1] < number):
	if (fib_numbers[-2]+fib_numbers[-1] < number):
		fib_numbers.append(fib_numbers[-2]+fib_numbers[-1])
	else:
		break

# Iterate for even numbers only
evenFibNumbers = []
for num in fib_numbers:
	if not num%2:
		evenFibNumbers.append(num)

# Present calculations
print("The sum of all even Fibonacci numbers below", number, "=", sum(evenFibNumbers))
