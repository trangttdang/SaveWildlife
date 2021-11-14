import matplotlib
from matplotlib import axes
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import shutil

def prediction_line(date, cases):
	A = np.array([np.arange(len(date))]).T
	b = np.array([cases]).T

	# create 
	lr = linear_model.LinearRegression()
	# fit (train the model)
	lr.fit(A,b)

	# p = ax + b
	# a or alpha is lr.coef_
	# b or beta is lr.intercept_
	x = np.array([[0, len(date)+30]]).T
	p = x*lr.coef_ + lr.intercept_
	return x, p

def predict_file(name , species):
	with open(name) as file:			# Open file
		data = file.read().split("\n")
		data.pop()						# Delete last rows

	header = data[0].split(",")			# Create lists
	Stat = data[1:]
	Date = []
	lst = []


	idx = header.index(species)
	for i in range(len(Stat)):		# Add item in lists
		Stat[i] = Stat[i].split(",")
		Date.append(Stat[i][0])
		lst.append(int(Stat[i][idx]))
	
	for i in range(2006,2022):			# Create time (Years)
		Date[i - 2006] = str(i)[-2:]

	fig = plt.figure()	
	fig, axs = plt.subplots()																		
	plt.suptitle("{} endangered prediction".format(species))								

	axs.xaxis.set_label_position('top')
	axs.plot(Date, np.array(lst), '.r', label = "species")					
	axs.xaxis.set_major_locator(plt.MultipleLocator(1))			
	axs.grid(color='black', ls = '-.', lw = 0.25)
	axs.set_xlabel("{} endangered".format(species), loc = 'left')	
	axs.set(ylabel = 'species')									
	x, p = prediction_line(Date, np.array(lst))
	axs.plot(x, p, '-', label = "prediction")
	plt.xlim(-1,19)
	axs.legend()


	
	file_name = species.lower() + ".jpg"
	fig.savefig(file_name, bbox_inches='tight', dpi=150)
	original = file_name
	target = 'static/images/' + file_name
	shutil.move(original,target)
	


