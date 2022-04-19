import os

from ._utils import Logger

class base():

	def __init__(self, df, **params):
		
		self.project_name = params.get('project_name', 'TheFile')
		self.time_col = params.get("time_col")
		self.ind_col = params.get("ind_col")
		
		self.check_linearity_dependent_independents = \
			params.get("check_linearity_dependent_independents", True)
		self.check_features_normal_dist = \
			params.get("check_features_normal_dist", True)
		self.check_multicollinearity = \
			params.get("check_multicollinearity", True)
		self.check_autocorrelation = \
			params.get("check_autocorrelation", True)
		self.check_heteroskedasticity = \
			params.get("check_heteroskedasticity", True)

		self.direc = f'./PyEconReg_reports/{self.project_name}'
		if not os.path.exists(self.direc):
			os.makedirs(self.direc)

		logging_address = os.path.join(self.direc, 'Report.log')
		self.log = Logger(logger_name = f'{self.project_name}-Logger',
							address = logging_address,
							mode='w')


		self.interact_cols = params.get("interact_cols")

		main_cols = list(df.columns)
		response_col = main_cols[-1]
		other_cols = main_cols[:-1]
		self.df = df
		if self.interact_cols:
			for col1, col2 in self.interact_cols:
				other_cols.append(f"{col1}-{col2}")
				self.df[f"{col1}-{col2}"] = df[col1] * df[col2]

		self.df = self.df[other_cols + [response_col]]


		