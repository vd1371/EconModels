import os
import numpy as np

import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
from statsmodels.stats.diagnostic import het_goldfeldquandt
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import het_breuschpagan

def _check_heteroskedasticity(**params):

	print ("Trying to _check_heteroskedasticity")

	tmp_df = params.get("df")
	main_direc = params.get("direc")
	log = params.get("log")
	ind_col = params.get("id_col")
	time_col = params.get("time_col")

	tmp_df = tmp_df.drop(columns = [ind_col, time_col], errors = 'ignore')

	X = np.asarray(tmp_df.iloc[:, :-1])
	Y = np.asarray(tmp_df.iloc[:, -1])
	X = sm.add_constant(X)

	report_str = "Goldfeld-Quandt homoskedasticity test."
	report_str += "The Null hypothesis is that the variance in the two sub-samples are the same.\n"
	fval, pval, alternative = het_goldfeldquandt(Y, X)
	if pval < 0.05:
		report_str += f"Null hypothesis rejected. The alternative: errors are {alternative}.\n\n"
	else:
		report_str += f"Null hypothesis not rejected.\n\n"


	report_str = "White’s Lagrange Multiplier Test for Heteroscedasticity"
	report_str += "Null (H0): Homoscedasticity is present. Alternative (HA). "+\
					"Heteroscedasticity is present\n"
	ols = OLS(Y, X).fit()
	ols_res = ols.resid
	_, pval, _, _ = het_white(ols_res, X)
	if pval < 0.05:
		report_str += f"Null hypothesis rejected. Alternative: Heteroscedasticity is present\n\n"
	else:
		report_str += f"Null hypothesis not rejected. No sufficient evidence to say heteroscedasticity is present.\n\n"


	_, pval, _, _ = het_breuschpagan(ols_res, X)
	report_str = "Breusch-Pagan Test for Heteroscedasticity"
	report_str += "Null (H0): Homoscedasticity is present. Alternative (HA). "+\
					"Heteroscedasticity is present\n"
	if pval < 0.05:
		report_str += f"Null hypothesis rejected. Alternative: Heteroscedasticity is present\n\n"
	else:
		report_str += f"Null hypothesis not rejected. No sufficient evidence to say heteroscedasticity is present.\n\n"

	log.info(report_str)