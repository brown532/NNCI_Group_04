import numpy as np
from data import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class Perceptron():
	def __init__(self):
		self.weights = []
		self.updated = False #checks if the weights were updating in the course of an epoch
		self.embedding_strengths = None

	def __local_potential(self,input,label): #E_mu
		e_mu = self.weights.dot(input)

		e_mu = e_mu * label

		return e_mu

	def plot_embedding_strengths(self):
		print(self.embedding_strengths)
		if self.embedding_strengths != None:
			# plt.hist(self.embedding_strengths,bins=len(self.embedding_strengths)+1,label='μQ_ls')
			x= np.arange(len(self.embedding_strengths))

			ax = plt.figure().gca()

			ax.bar(x, height=self.embedding_strengths)
			plt.xticks(x, x+1)

			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Sample (μ)")
			plt.ylabel("Fraction of successful runs")

			plt.legend(loc='upper right')
			plt.show()

	def train(self,data,labels,epochs,c=0,homogeneous=True,use_embedding_strength=False): #fit model to training data
		#initialize weights
		self.updated = False
		self.weights = np.zeros(data.shape[1] + (1-int(homogeneous))) #adds clamped input for inhomogeneous cases

		if not homogeneous:
			clamps = [[-1]] * len(labels)
			data=np.append(data,clamps,axis=1)


		if use_embedding_strength:
			self.embedding_strengths = [0]*len(labels)

		for epoch in range(0,epochs):
			self.updated = False
			# print("epoch "+str(epoch)+":")
			for sample_index,sample in enumerate(data):
				if self.__local_potential(sample,labels[sample_index]) <= c:
					self.updated = True

					# self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)

					if use_embedding_strength:
						self.embedding_strengths[sample_index] += 1

						self.weights = [0]*len(self.weights)
						for datum_index,datum in enumerate(data): 
							self.weights += datum*(self.embedding_strengths[datum_index]*labels[datum_index]/data.shape[1])

					else:
						self.weights = self.weights + ((sample * labels[sample_index]) / sample.shape)




			if self.updated == False:
				print(self.weights)


				if use_embedding_strength:
					print(self.embedding_strengths)

				print(epoch)
				return True

		return False


x = Population(alpha=1.8, mean=0, variance=1, number_of_features=20)

model = Perceptron()

model2 = Perceptron()
# print(x.dataset)
b = model.train(data = x.dataset, labels = x.label, epochs = 100,use_embedding_strength=True)
print("===========================")
# c = model2.train(data = x.dataset, labels = x.label, epochs = 100,use_embedding_strength=False)


# model2.plot_embedding_strengths()


# print("plotting model1")

model.plot_embedding_strengths()

