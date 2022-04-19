import matplotlib.pyplot as plt

def _draw_heteroskedasticity(df, res, directory):

	file_counter = 0

	fig, ax = plt.subplots(nrows=2, ncols=2)
	fig.tight_layout()
	for i, col in enumerate(df.columns):

		counter = i % 4
		row_idx = int (counter/2)
		col_idx = counter % 2

		ax[row_idx, col_idx].set_title(col)
		ax[row_idx, col_idx].scatter(df[col], res, s = 1)

		if (i % 4 == 3) or (i == len(df.columns)-1):
			
			plt.savefig(f"{directory}/Hetero-{file_counter}.png")
			plt.close()

			file_counter += 1
			if i != len(df.columns)-1:
				fig, ax = plt.subplots(nrows=2, ncols=2)
				fig.tight_layout()