import os
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS

from ._check_assumps_after_analysis import check_assumps_after_analysis

def _run_OLS(**params):

	print ("Trying to _run_OLS")

	tmp_df = params.get("df")
	main_direc = params.get("direc")
	log = params.get("log")
	ind_col = params.get("id_col")
	time_col = params.get("time_col")

	directory = f"{main_direc}/OLS"
	if not os.path.exists(directory):
		os.makedirs(directory)

	tmp_df = tmp_df.drop(columns = [ind_col, time_col], errors = 'ignore')

	X = np.asarray(tmp_df.iloc[:, :-1])
	Y = np.asarray(tmp_df.iloc[:, -1])
	X = sm.add_constant(X)
	  
	ols = OLS(Y, X).fit()
	ols_res = ols.resid

	summary = ols.summary()
	report_str = "Simple OLS\n\n"
	report_str += summary.__str__()

	log.info(report_str)

	check_assumps_after_analysis(tmp_df, ols_res, directory, log)