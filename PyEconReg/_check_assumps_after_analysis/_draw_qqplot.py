import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def _draw_qqplot(df, res, directory):

	plt.clf()
	sm.qqplot(res, loc = np.mean(res), scale = np.std(res), line ='45')
	plt.savefig(f"{directory}/ResidualsQQPlot.png")