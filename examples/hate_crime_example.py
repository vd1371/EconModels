import pandas as pd
from linearmodels.datasets import wage_panel

from PyEconReg import PyEconReg

def run_hate_crime_example():

	df = pd.read_csv("./examples/HateCrime.csv")

	quarter = [f"{t[:4]}-{int(t[-1])*3}-30" for t in df['quarter']]
	df['quarter'] = pd.to_datetime(quarter)
	df.fillna(0, inplace = True)

	reg = PyEconReg(df,
					project_name = 'HateQuarter',
					time_col = 'quarter',
					ind_col = 'czone',
					response_col = 'hatec_over_pop',
					check_linearity_dependent_independents = False,
					check_features_normal_dist = False,
					check_multicollinearity = False,
					check_autocorrelation = False,
					check_heteroskedasticity = False,
					interact_cols = [['trump_period_dummy', 'd_tradeusch_pw_2012_1999']],
					)
	reg.check_assumps_before_analysis()
	reg.run_panel_OLS()