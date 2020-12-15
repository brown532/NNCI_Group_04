import matplotlib.pyplot as plt
import math 

def Pls(P,N):
	if P<=N:
		return 1
	else:
		summation = 0

		for i in range(0,N-1):
			# ans = (P-1)!/(i! * (P-1 - i)!)

			summation += math.factorial(P-1)/(math.factorial(i) * math.factorial(P-1 - i))
			# print(summation)

			# summation += ans

		summation *= 2**(1-P)

		return summation

# alphas = [0.75]

# while alphas[-1] < 3.0:
# 	alphas.append(alphas[-1] + 0.05)


# # print(alphas)

# N = 300


# P_ls = []
# for alpha in alphas:
# 	print(alpha)
# 	P = int(alpha * N-1)

# 	P_ls.append(Pls(P,N))

# plt.plot(alphas,P_ls, marker='.',color ='red')


# N = 30


# P_ls = []
# for alpha in alphas:
# 	print(alpha)
# 	P = int(alpha * N-1)

# 	P_ls.append(Pls(P,N))

# plt.plot(alphas,P_ls, marker='.',color ='blue')


# N = 5


# P_ls = []
# for alpha in alphas:
# 	print(alpha)
# 	P = int(alpha * N-1)

# 	P_ls.append(Pls(P,N))

# plt.plot(alphas,P_ls, marker='.',color ='green')


# plt.show()
