from .base import base

class PyEconReg(base):

	def __init__(self, df, project_name = 'TheFile', **params):
		'''
		df: A dataframe consisting the dependent and independent variables
			It is assumed that the last column of the data is the independent
			variable to be predicted/estimated
		time_col: The name of the column consisting the time factor
		ind_col: The name of the column consisting the individuals

		'''
		super().__init__(project_name)
		
		self.df = df
		self.time_col = params.get("time_col")
		self.ind_col = params.get("ind_col")


	def run(self):
		pass

	def run_OLS(self):
		pass

	def run_FE_regression(self):
		pass

	def run_RE_regression(self):
		pass

	def optimize(self):
		pass

	def check_assumps_before_analysis(self):
		## Draw Scatter Plot
		## Draw histogram of feature and check goodness of fit
		## Check multi-collinearity
		#### Correlation matrix
		#### Check tolerance
		#### Check variance inflation factor
		## Check autocorrelation: Think more about it
		## Condition index
		pass

	def check_assumps_after_analysis(self):
		# https://people.duke.edu/~rnau/testing.htm
		## Durbin Watson on residuals + Plots of residuals
		## Homoscedasticity: Scatter plot + Goldfeld-Quandt
		## Normality of errors: Zero mean + Distribution
		## Error term against response
		pass