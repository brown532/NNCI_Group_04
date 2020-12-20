import matplotlib.pyplot as plt

from data import Population
from Perceptron import Perceptron


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



c_values = [0,0.05,0.1,0.2]


for c in c_values:
	print("using",c)

	initial_alpha_value = 0.75

	alpha_values = []

	Q_ls = []

	while initial_alpha_value<=final_alpha_value:
		Q_ls.append(0)
		for random_population in range(0,n_D):	
			x = Population(alpha=initial_alpha_value, mean=mean, variance=variance, number_of_features=number_of_features)

			model = Perceptron()

			# print(x.dataset)
			if model.train(data = x.dataset, labels = x.label, epochs = n_max,c=c):
				Q_ls[-1] += 1


		alpha_values.append(initial_alpha_value)
		initial_alpha_value += increment

	Q_ls = [x/n_D for x in Q_ls]
	plt.plot(alpha_values,Q_ls, marker='o',label='c='+str(c))

	print(Q_ls)



plt.xlabel("P/N")
plt.ylabel("Fraction of successful runs")

plt.legend(loc='upper right')
plt.show()

# print(Q_ls)
# print(alpha_values)