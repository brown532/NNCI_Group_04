import matplotlib.pyplot as plt
import math 

def Pls(P,N):
	if P<=N:
		return 1
	else:
		summation = 0

		for i in range(0,N-1):
			summation += math.factorial(P-1)/(math.factorial(i) * math.factorial(P-1 - i))
		summation *= 2**(1-P)

		return summation
