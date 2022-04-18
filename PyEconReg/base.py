import os

from ._utils import Logger

class base():

	def __init__(self, project_name, **params):
		self.project_name = params.get('project_name', 'TheFile')
		
		self.direc = f'./PyEconReg_reports/{self.project_name}'
		if not os.path.exists(self.direc):
			os.makedirs(self.direc)

		logging_address = os.path.join(self.direc, 'Report.log')
		self.log = Logger(logger_name = f'{self.project_name}-Logger',
							address = logging_address,
							mode='a')
		