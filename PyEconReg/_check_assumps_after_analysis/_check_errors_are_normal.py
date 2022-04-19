import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

def _check_errors_are_normal(res, log, directory):

	report_str = "Check if errors follow normal distribution by Kolmogorov-Smirnov test\n\n"
	ktest = kstest(res, 'norm', args=(np.mean(res), np.std(res)))
	report_str += f"Residuals | Mean: {np.mean(res):.3f} | "

	if ktest.pvalue < 0.05:
		report_str += "Null Hyp Rejected - Normal Dist: NO"
	else:
		report_str += "Null Hyp Not Rejectd - Normal Dist: Possibly"
	report_str += " | " + ktest.__str__() + "\n"
	log.info(report_str)

	plt.clf()
	plt.hist(res)
	plt.xlabel('Residuals')
	plt.savefig(f"{directory}/ResidualsHistogram.png")