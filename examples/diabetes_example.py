from sklearn.datasets import load_diabetes
from PyEconReg import PyEconReg

def run_diabetes_example():

	data = load_diabetes(as_frame = True).frame

	myModel = PyEconReg(data,
						project_name = 'DiabetesTest',
						time_col = 'age')
	myModel.check_assumps_before_analysis()
	myModel.run_OLS()