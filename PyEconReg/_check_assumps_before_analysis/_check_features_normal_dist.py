import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

def _check_features_normal_dist(**params):

	print ("Trying to _check_features_normal_dist")

	df = params.get("df")
	main_direc = params.get("direc")
	log = params.get("log")

	directory = f"{main_direc}/condition_check_normal_dist"
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	report_str = "Check if the feature follow normal distribution by Kolmogorov-Smirnov test\n\n"
	for i, col in enumerate(df.columns):

		try:
			l = len(col)

			ktest = kstest(df[col], 'norm',
							args=(np.mean(df[col]), np.std(df[col])))
			report_str += f"F1-{col[:min(l, 10)]}"
			for j in range(12-min(l, 10)):
				report_str += " "
			report_str += "| "

			if ktest.pvalue < 0.05:
				report_str += "Null Hyp Rejected - Normal Dist: NO"
			else:
				report_str += "Null Hyp Not Rejectd - Normal Dist: Possibly"
			report_str += " | " + ktest.__str__() + "\n"
		except TypeError:
			pass

		plt.clf()
		plt.hist(df[col])
		plt.xlabel(col)
		plt.savefig(f"{directory}/F{i}-{col}.png")

	log.info(report_str)