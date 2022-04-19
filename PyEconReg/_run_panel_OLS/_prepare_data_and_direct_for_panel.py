import os
import pandas as pd

def _prepare_data_and_direct_for_panel(time_effect = False,
										model_name = "Unknown",
										**params):

	df = params.get("df").copy()
	main_direc = params.get("direc")
	ind_col = params.get("ind_col")
	time_col = params.get("time_col")

	if time_col == None or ind_col == None:
		raise ValueError ("ind_col and time_col can't be None.")

	time_effect = "-WithTimeEffect" if time_effect else ""
	directory = f"{main_direc}/{model_name}OLS{time_effect}"
	if not os.path.exists(directory):
		os.makedirs(directory)

	time_info = pd.Categorical(df[time_col])
	data = df.set_index([ind_col, time_col])

	if time_effect:
		main_cols = list(data.columns)
		data[time_col] = time_info
		data = data[main_cols[:-1] + [time_col] + [main_cols[-1]]]

	return data, directory