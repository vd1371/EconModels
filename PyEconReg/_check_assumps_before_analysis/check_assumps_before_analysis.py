from ._check_linearity_dependent_independents import _check_linearity_dependent_independents
from ._check_features_normal_dist import _check_features_normal_dist
from ._check_multicollinearity import _check_multicollinearity
from ._check_autocorrelation import _check_autocorrelation
from ._check_heteroskedasticity import _check_heteroskedasticity

def check_assumps_before_analysis(**params):

	check_linearity_dependent_independents = \
		params.get("check_linearity_dependent_independents")
	check_features_normal_dist = \
		params.get("check_features_normal_dist")
	check_multicollinearity = \
		params.get("check_multicollinearity")
	check_autocorrelation = \
		params.get("check_autocorrelation")
	check_heteroskedasticity = \
		params.get("check_heteroskedasticity")

	if check_linearity_dependent_independents:
		_check_linearity_dependent_independents(**params)

	if check_features_normal_dist:
		_check_features_normal_dist(**params)
	
	if check_multicollinearity:
		_check_multicollinearity(**params)
	
	if check_autocorrelation:
		_check_autocorrelation(**params)
	
	if check_heteroskedasticity:
		_check_heteroskedasticity(**params)

