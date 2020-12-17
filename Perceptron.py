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

	def train(self,data,labels,epochs,c=0,homogeneous=True,embedding_strength=False): #fit model to training data
		#initialize weights
		self.weights = np.zeros(data.shape[1] + (1-int(homogeneous))) #adds clamped input for inhomogeneous cases

		if not homogeneous:
			clamps = [[-1]] * len(labels)
			data=np.append(data,clamps,axis=1)


		if embedding_strength:
			self.embedding_strengths = [0]*len(labels)

		print(self.embedding_strengths)

		for epoch in range(0,epochs):
			self.updated = False
			# print("epoch "+str(epoch)+":")
			for sample_index,sample in enumerate(data):
				if self.__local_potential(sample,labels[sample_index]) <= c:
					self.updated = True

					self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)

					if embedding_strength:
						self.embedding_strengths[sample_index] += 1



			if self.updated == False:
				print(self.weights)


				temp_weights = [0]*len(self.weights)

				#calculates weights from embedding strengths
				for datum_index,datum in enumerate(data): 
					temp_weights += datum*(self.embedding_strengths[datum_index]*labels[datum_index]/data.shape[1])

				# temp_weights/=data.shape[1]

				print(temp_weights)



				print(self.embedding_strengths)
				print(epoch)
				return True

		return False


x = Population(alpha=0.8, mean=0, variance=1, number_of_features=5)

model = Perceptron()

# print(x.dataset)
b = model.train(data = x.dataset, labels = x.label, epochs = 100,embedding_strength=True)

print(b)

