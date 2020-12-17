import matplotlib.pyplot as plt

from data import Population
from Perceptron import Perceptron

from test import *


#parameters for experiments:

#Population:
mean = 0
variance = 1.0
number_of_features = 20

n_D = 500 #Number of populations created
n_max = 100 #maximum number of epochs for perceptron to find a solution

#
#Experiment loop
initial_alpha_value = 0.75
final_alpha_value = 3.0
increment = 0.25


for homogeneous_value in [True,False]:
	print("using",homogeneous_value)

	initial_alpha_value = 0.75

	alpha_values = []

	Q_ls = []

	while initial_alpha_value<=final_alpha_value:
		Q_ls.append(0)
		for random_population in range(0,n_D):	
			x = Population(alpha=initial_alpha_value, mean=mean, variance=variance, number_of_features=number_of_features)

			model = Perceptron()

			# print(x.dataset)
			if model.train(data = x.dataset, labels = x.label, epochs = n_max,homogeneous=homogeneous_value):
				Q_ls[-1] += 1


		alpha_values.append(initial_alpha_value)
		initial_alpha_value += increment

	Q_ls = [x/n_D for x in Q_ls]
	if homogeneous_value:
		plt.plot(alpha_values,Q_ls, marker='o',label='without clamped input')
	else:
		plt.plot(alpha_values,Q_ls, marker='o',label='with clamped input')

	print(Q_ls)



plt.xlabel("P/N")
plt.ylabel("Fraction of successful runs")

plt.legend(loc='upper right')
plt.show()

# print(Q_ls)
# print(alpha_values)