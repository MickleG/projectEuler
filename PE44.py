# Pentagonal numbers are generated by the formula, P_n=n(3n-1)/2. 
# The first ten pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. 
# However, their difference, 70 - 22 = 48, is not pentagonal.
# Find the pair of pentagonal numbers, P_j and P_k, 
# for which their sum and difference are pentagonal and 
# D = |P_k - P_j| is minimised; what is the value of D?
import math
import time

pentagonals = []
solution_found = False
pentagonals_size = 2

Pk = 0
Pj = 0

def isPentagonal(P):
	if(((1 + math.sqrt(1 + 24 * P)) / 6) % 1 == 0):
		return True
	else:
		return False

def genPentagonals(size):
	global pentagonals

	pentagonals = []
	for i in range(1, size + 1):
		pentagonals.append(i * (3 * i - 1) / 2)




while solution_found == False:
	genPentagonals(pentagonals_size)

	# print(pentagonals)

	for item1 in pentagonals:

		for item2 in pentagonals:
			if(item1 == item2):
				break

			if((item2 - item1 in pentagonals) and (item2 + item1 in pentagonals)):
				print(item1, item2)
				solution_found = True
				Pj = item1
				Pk = item2

				break

	pentagonals_size += 100

	print("size of pentagonals is ", pentagonals_size)

print(Pk - Pj)