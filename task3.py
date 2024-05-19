import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("*********** TASK 3 ***********")

# Read the data set.
df = pd.read_csv("train.csv")

# Find the numbers of columns with numbers.
cnt = 0
for title in df.head(0):
	type = df.dtypes[title]
	if type == "int64" or type == "float64":
		cnt += 1

# Create a histogram for every numerical column.
fig, (cols) = plt.subplots(1, cnt)
num_col_index = 0
for title in df.head(0):
	# Verify if the column is numerical.
	type = df.dtypes[title]
	if type != "int64" and type != "float64":
		continue
	# Options.
	col = df[title]
	options = set(col)
	dict_options = {}
	index = 0
	for option in options:
		if np.isnan(option) == 0 and option not in dict_options.keys():
			dict_options[option] = index
			index += 1
	# Counters.
	cnt = np.full(len(options), 0)
	for elem in col:
		if np.isnan(elem) == 0:
			index = dict_options.get(elem)
			cnt[index] += 1
	# Histogram 
	cols[num_col_index].hist(options, len(options), color = "red", weights = cnt)
	cols[num_col_index].set_title(title)
	num_col_index += 1

# Print the histograms.
fig.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()
