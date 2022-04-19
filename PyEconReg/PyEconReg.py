from .base import base
from ._check_assumps_before_analysis import check_assumps_before_analysis
from ._run_OLS import _run_OLS
from ._run_panel_OLS import run_panel_OLS

class PyEconReg(base):

	def __init__(self, df, **params):
		'''
		df: A dataframe consisting the dependent and independent variables
			It is assumed that the last column of the data is the independent
			variable to be predicted/estimated
		time_col: The name of the column consisting the time factor
		ind_col: The name of the column consisting the individuals

		'''
		super().__init__(df, **params)

	def check_assumps_before_analysis(self):
		check_assumps_before_analysis(**self.__dict__)

	def run_OLS(self):
		_run_OLS(**self.__dict__)

	def run_panel_OLS(self):
		run_panel_OLS(**self.__dict__)

	def optimize(self):
		pass

	