#The fraction 49/98 is a curious fraction, as an inexperienced 
# mathematician in attempting to simplify it may incorrectly believe 
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and 
# denominator.

# If the product of these four fractions is given in its lowest common 
# terms, find the value of the denominator.

product = 1

for denom in range(10, 100):
	for num in range(10, 100):
		for str_digit in str(num):
			if((str_digit in str(denom)) and int(str_digit) > 0):
				result1 = num / denom

				removed_denom = str(denom).replace(str_digit, '', 1)
				removed_num = str(num).replace(str_digit, '', 1)

				if(int(removed_denom) == 0):
					break

				result2 = int(removed_num) / int(removed_denom)

				if(result1 == result2) and result1 < 1:
					print(num, '/', denom)
					product *= result1

print(product)
