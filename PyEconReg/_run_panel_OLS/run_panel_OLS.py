import pandas as pd
from ._run_pooled_ols import _run_pooled_ols
from ._run_random_effects import _run_random_effects
from ._run_fixed_effects import _run_fixed_effects

def run_panel_OLS(**params):

	print ("Trying to _run_panel_OLS")

	main_direc = params.get("direc")
	log = params.get("log")

	_run_pooled_ols(time_effect = False, **params)
	_run_pooled_ols(time_effect = True, **params)
	_run_random_effects(time_effect = False, **params)
	_run_random_effects(time_effect = True, **params)
	_run_fixed_effects(time_effect = False, **params)
	_run_fixed_effects(time_effect = True, **params)


	