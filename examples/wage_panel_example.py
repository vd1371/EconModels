import pandas as pd
from linearmodels.datasets import wage_panel

from PyEconReg import PyEconReg

def run_wage_example():

	data = wage_panel.load()
	# data = data.set_index(["nr", "year"])

	myModel = PyEconReg(data,
						project_name = 'WageDataSet',
						time_col = 'year',
						ind_col = 'nr',
						interact_cols = [['exper', 'hours']])
	myModel.check_assumps_before_analysis()
	myModel.run_panel_OLS()