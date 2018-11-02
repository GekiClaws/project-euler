
# Difference between the sum of the squares of
# the first one hundred natural numbers 
# and the square of the sum

sum_of_squares = 0

for x in range(1, 101):
	sum_of_squares += x**2

squared_sum = 0
for x in range(1, 101):
	squared_sum += x

squared_sum **= 2

print(squared_sum-sum_of_squares)