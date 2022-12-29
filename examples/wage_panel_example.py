import pandas as pd
from linearmodels.datasets import wage_panel

from PyEconReg import PyEconReg

def run_wage_example():

	df = wage_panel.load()
	# data = data.set_index(["nr", "year"])

	myModel = PyEconReg(df,
						project_name = 'WageDataSet',
						time_col = 'year',
						ind_col = 'nr',
						response_col = "lwage",
						interact_cols = [['exper', 'hours']])
	myModel.check_assumps_before_analysis()
	myModel.run_panel_OLS()