digits = 6
counter = 0


for j in range(10**(digits - 1), 10**(digits)):
	digit_array = []
	first_sum = 0
	second_sum = 0

	for digit in str(j):
		digit_array.append(int(digit))
	for i in range(int(digits / 2)):
		first_sum = first_sum + digit_array[i]
	for i in range(int(digits / 2), len(digit_array)):
		second_sum = second_sum + digit_array[i]
	if(first_sum == second_sum):
		#print(j)
		counter = counter + 1

print(digits, counter)