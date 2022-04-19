import os
import matplotlib.pyplot as plt

def _check_linearity_dependent_independents(**params):

	print ("Trying to _check_linearity_dependent_independents")

	df = params.get("df")
	main_direc = params.get("direc")

	directory = f"{main_direc}/condition_check_linearity"
	if not os.path.exists(directory):
		os.makedirs(directory)

	X, Y = df.iloc[:, :-1], df.iloc[:, -1]
	
	for i, col in enumerate(X.columns):
		plt.clf()
		plt.scatter(X[col], Y)
		plt.xlabel(col)
		plt.ylabel(df.columns[-1])
		plt.savefig(f"{directory}/F{i}-{col}.png")