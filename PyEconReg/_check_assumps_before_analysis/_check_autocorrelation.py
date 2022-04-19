import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson
from statsmodels.regression.linear_model import OLS
from statsmodels.graphics.tsaplots import plot_acf , plot_pacf

def _check_autocorrelation(**params):

	print ("Trying to _check_autocorrelation")

	df = params.get("df")
	main_direc = params.get("direc")
	log = params.get("log")
	time_col = params.get("time_col")
	ind_col = params.get("ind_col")

	tmp_df = df.drop(columns = [time_col, ind_col], errors = 'ignore')

	if not time_col == None:

		tmp_df = df.sort_values(by = time_col)

		directory = f"{main_direc}/condition_check_autocorrelation"
		if not os.path.exists(directory):
			os.makedirs(directory)

		plt.clf()
		plot_acf(tmp_df.iloc[:, -1], alpha =0.05, lags=50)
		plt.savefig(f"{directory}/AutoCorrelation.png")

		plt.clf()
		plot_pacf(tmp_df.iloc[:, -1], alpha =0.05, lags=50)
		plt.savefig(f"{directory}/PartialAutoCorrelation.png")
		  
		"""
		Code for Durbin Watson test
		"""
		X = np.arange(len(df))
		Y = np.asarray(df.iloc[:, -1])
		X = sm.add_constant(X)
		  
		ols_res = OLS(Y,X).fit()
		durbin = durbin_watson(ols_res.resid)

		report_str = "Durbin-Watson test for checking autocorrelation\n"
		report_str += "D between 0 and 4. D around 2 indicate no autocorrelation.\n"
		report_str += "As a rule of thumb values: 1.5 < d < 2.5 show" +\
						" that there is no auto-correlation in the data.\n\n"
		report_str += f"Durbin-Watson value: {durbin:.2f}: "
		if 1.5 < durbin and durbin < 2.5:
			report_str += "No auto-correlation in the data.\n"
		else:
			report_str += "Possible auto-correlation in the data.\n"

		log.info(report_str)