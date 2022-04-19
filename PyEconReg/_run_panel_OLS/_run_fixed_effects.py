import statsmodels.api as sm
from linearmodels.panel import PanelOLS

from ._prepare_data_and_direct_for_panel import _prepare_data_and_direct_for_panel
from .._check_assumps_after_analysis import check_assumps_after_analysis

def _run_fixed_effects(time_effect = False, **params):

	print ("Trying to _run_fixed_effects")

	data, directory = _prepare_data_and_direct_for_panel(time_effect,
														"FixedEffect",
														**params)

	log = params.get("log")

	exog = sm.add_constant(data.iloc[:, :-1])
	mod = PanelOLS(data.iloc[:, -1], exog,
					entity_effects = True, drop_absorbed=True)
	pooled_res = mod.fit()

	res = pooled_res._resids.reshape(-1)

	report_str = "FixedEffect\n\n"
	report_str += pooled_res.__str__()

	log.info(report_str)

	check_assumps_after_analysis(data, res, directory, log)