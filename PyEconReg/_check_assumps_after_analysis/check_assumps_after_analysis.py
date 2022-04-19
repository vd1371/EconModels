from ._draw_heteroskedasticity import _draw_heteroskedasticity
from ._check_errors_are_normal import _check_errors_are_normal
from ._draw_qqplot import _draw_qqplot

def check_assumps_after_analysis(df, res, directory, log):

	_draw_heteroskedasticity(df, res, directory)
	_check_errors_are_normal(res, log, directory)
	_draw_qqplot(df, res, directory)

