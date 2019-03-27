
##############
# Question 1 #
##############
# Define sort function
# I implemented the classic selection sort algorithm, since for small data
# (like the test set), it should even perform better than quicksort or mergesort.
def sort_list(l):
	for i in range(len(l)):
		min = i
		for j in range(i+1, len(l)):
			if l[min] > l[j]:
				min = j

		l[i], l[min] = l[min], l[i]

	return l

##############
# Question 2 #
##############
# Given a random number and a random digit, design an algorithm to place the 
# digit so that the number is divisible by 3
def div7(n, i):
	for idx in range(len(str(n))+1):
		numstr = str(n)
		num = int(numstr[:idx] + str(i) + numstr[idx:])
		if num%7 == 0:
			return num
	raise Exception('not possible')

##############
# Question 3 #
##############
# Extend the cubic function y = a_1 x^3 + a_2 x^2 + a_3 x + a_4 to handle a 
# multi-variate input
def cubic(x, A):
	import numpy as np
	x1 = x
	x2 = x1*x
	x3 = x2*x
	return sum([np.dot(x3,A[0,:]), np.dot(x2,A[1,:]), np.dot(x1,A[2,:]), np.dot(np.ones(len(x)),A[3,:])])
	


