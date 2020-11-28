import numpy as np
from matplotlib import pyplot as plt
import random


class Population():
	
	def __init__(self,size=10,mean=0,variance=1.0,number_of_features=5):
		self.dataset = self.generate_attribute(size,mean,variance)

		for x in range(0,number_of_features-1):
			self.dataset = np.append(self.dataset,self.generate_attribute(size,mean,variance),axis=1)


		self.label = []

		for x in range(0,size):
			class_label = random.randint(1,2)

			if class_label == 1:
				self.label.append(-1)
			else:
				self.label.append(1)


	def generate_attribute(self,number_of_samples,mean,variance):
		desired_std_dev = variance**0.5

		samples = np.random.normal(loc=0.0, scale=desired_std_dev, size=number_of_samples)

		#generate samples
		actual_mean = np.mean(samples)
		actual_std = np.std(samples)
		
		#subtract the mean of generated samples
		samples = samples - (actual_mean)

		#scale samples to get exact desired variance/standard deviation
		new_std = np.std(samples)
		samples = samples * (desired_std_dev/new_std)

		#add desired mean to the data to get exact desired mean
		final_samples = samples + mean

		return np.array(final_samples).reshape(len(final_samples),1)

	

	def plot(self,attributes_to_plot):
		x_axis = list(range(1,self.dataset.shape[0]+1))

		ax = plt.gca()

		for x in range(0,attributes_to_plot):
			y_axis = self.dataset[:,x]

			ax.scatter(x_axis,y_axis,marker='.',label="attribute "+str(x))#color=(random.random(),random.random(),random.random()))

		plt.xlabel('Sample')
		# Set the y axis label of the current axis.
		plt.ylabel('Value')
		# Set a title of the current axes.
		plt.title('First '+str(attributes_to_plot) + 'attributes of the dataset')
		# show a legend on the plot
		plt.legend()
		# Display a figure.
		plt.show()



# pop = Population(size=10 ,mean=0,variance=1.0,number_of_features=3)

# print(pop.dataset)

# print("mean: ",np.mean(pop.dataset[:,0]))

# print("variance: ",np.var(pop.dataset[:,0]))

# print(pop.label)
# pop.plot(11)