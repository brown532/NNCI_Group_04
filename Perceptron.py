import numpy as np
from data import Population

class Perceptron():
	def __init__(self):
		self.inputs = []
		self.weights = []
		self.output = None #S

	def __local_potential(self,input,label): #E_mu
		e_mu = self.weights.dot(input)

		e_mu = e_mu * label

		return e_mu

	def fit(self,data,labels,epochs): #fit model to training data
		#initialize weights
		self.weights = np.zeros(data.shape[1])


		for epoch in range(0,epochs):
			print("epoch "+str(epoch)+":")
			for sample_index,sample in enumerate(data):
				if self.__local_potential(sample,labels[sample_index]) <= 0:

					print("updating weights")

					# print(self.weights)
					self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)

					# print("=====> ",self.weights)


			print("======================")

		#for number of epochs:
			#for sample in population:
				#if (local potential) <= 0:
					#update weight vector

				#else:
					#pass

		pass

	def predict(self):
		pass



x = Population(size = 100, mean=0, variance=1.0, number_of_features=65)

model = Perceptron()

model.fit(data = x.dataset, labels = x.label, epochs = 1000)


# x = np.ones(5)*3

# print(x)

# x =1.2+x.dot(2)

# print(x)