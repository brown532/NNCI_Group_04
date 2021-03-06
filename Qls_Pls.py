import matplotlib.pyplot as plt

from data import Population
from Perceptron import Perceptron

from Pls import *


#parameters for experiments:

#Population:
mean = 0
variance = 1.0
number_of_features = 20

n_D = 50 #Number of populations created
n_max = 100 #maximum number of epochs for perceptron to find a solution

#
#Experiment loop
initial_alpha_value = 0.75
final_alpha_value = 3.0
increment = 0.25

alpha_values = []

Q_ls = []

P_ls = []

while initial_alpha_value<=final_alpha_value:
	Q_ls.append(0)
	for random_population in range(0,n_D):	
		x = Population(alpha=initial_alpha_value, mean=mean, variance=variance, number_of_features=number_of_features)

		model = Perceptron()

		# print(x.dataset)
		if model.train(data = x.dataset, labels = x.label, epochs = n_max):
			Q_ls[-1] += 1


	P_ls.append(Pls(int(initial_alpha_value*number_of_features),number_of_features))

	alpha_values.append(initial_alpha_value)
	initial_alpha_value += increment



Q_ls = [x/n_D for x in Q_ls]
plt.plot(alpha_values,Q_ls, marker='o',label='Q_ls')

plt.plot(alpha_values,P_ls,marker='o',label='P_ls')

plt.xlabel("P/N")
plt.ylabel("Fraction of successful runs")

plt.legend(loc='upper right')
plt.show()
