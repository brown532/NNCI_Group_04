import numpy as np
from data import *
import matplotlib.pyplot as plt

class Perceptron():
	def __init__(self):
		self.weights = []
		self.updated = False #checks if the weights were updating in the course of an epoch

	def __local_potential(self,input,label): #E_mu
		e_mu = self.weights.dot(input)

		e_mu = e_mu * label

		return e_mu

	def train(self,data,labels,epochs,c=0): #fit model to training data
		#initialize weights
		self.weights = np.zeros(data.shape[1])

		# print(len(labels))

		for epoch in range(0,epochs):
			self.updated = False
			# print("epoch "+str(epoch)+":")
			for sample_index,sample in enumerate(data):
				# print(sample_index)
				# print(sample)
				# print(labels[sample_index])
				# print("============================")
				if self.__local_potential(sample,labels[sample_index]) <= c:
					self.updated = True

					self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)

					# print("=====> ",self.weights)


			if self.updated == False:
				return True

		return False


# x = Population(size= 9 , mean=0, variance=1.0, number_of_features=10)

# model = Perceptron()

# if model.train(data = x.dataset, labels = x.label, epochs = 100):
# 	count += 1


# print(count)