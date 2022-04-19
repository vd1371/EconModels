import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

def _check_multicollinearity(**params):

	print ("Trying to _check_multicollinearity")

	df = params.get("df")
	ind_col = params.get("id_col")
	time_col = params.get("time_col")
	tmp_df = df.drop(columns = [ind_col, time_col], errors = 'ignore')
	main_direc = params.get("direc")
	log = params.get("log")

	directory = f"{main_direc}/condition_multicollinearity"
	if not os.path.exists(directory):
		os.makedirs(directory)

	report_str = "--- Check if there is multicollinearity among independent variables ---\n\n"

	######### Checking the correlation matrix and drawing heatmap
	corr = tmp_df.corr()
	report_str += "Pairwise Correlation Matrix\n\n"
	report_str += corr.to_string() + "\n\n\n"

	report_str += "Tolerance: 1-R2. T < 0.1 there might be multicollinearity, T < 0.01 there certainly is.\n"
	report_str += "VIF: Variance inflation factor. VIF > 5 indication that multicollinearity may be present; with VIF > 10 there certainly is.\n"

	plt.clf()
	cmap = sns.diverging_palette(500, 10, as_cmap=True)
	ans=sns.heatmap(corr,  linewidths=1, cmap=cmap, center=0)
	figure = ans.get_figure()    
	figure.savefig(f"{directory}/CorrHeatMap.png")
	
	X = tmp_df.iloc[:, :-1]
	for i, col in enumerate(X.columns):


		x = X.loc[:, X.columns[~X.columns.isin([col])]]
		y = X.loc[:, col]

		reg = LinearRegression().fit(x, y)
		r2 = reg.score(x, y)

		l = len(col)
		report_str += f"F1-{col[:min(l, 10)]}"
		for j in range(12-min(l, 10)):
			report_str += " "
		report_str += "| "

		report_str += f" Tolerance: {1-r2:.2f} - VIF:{1/(1-r2):.2f} - "
		if r2 > 0.9:
			report_str += "Strong multicollinearity\n"
		elif r2 > 0.8:
			report_str += "Possible multicollinearity\n"
		else:
			report_str += "Weak multicollinearity\n"

	log.info(report_str)