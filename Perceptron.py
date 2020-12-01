import numpy as np

import matplotlib.pyplot as plt

class Perceptron():
	def __init__(self):
		self.weights = []
		self.updated = False #checks if the weights were updating in the course of an epoch

	def __local_potential(self,input,label): #E_mu
		e_mu = self.weights.dot(input)

		e_mu = e_mu * label

		return e_mu

	def fit(self,data,labels,epochs): #fit model to training data
		#initialize weights
		self.weights = np.zeros(data.shape[1])


		for epoch in range(0,epochs):
			self.updated = False
			# print("epoch "+str(epoch)+":")
			for sample_index,sample in enumerate(data):
				if self.__local_potential(sample,labels[sample_index]) <= 0:
					self.updated = True

					# print("updating weights")

					# print(self.weights)
					self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)

					# print("=====> ",self.weights)


			if self.updated == False:
				return True

		return False
