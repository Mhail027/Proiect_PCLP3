import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("*********** TASK 8 ***********")

# Read the data set.
df = pd.read_csv("train.csv")

# Find the medium age for survivors and deads.
survs_added_age = 0
deads_added_age = 0
survivors = 0
deads = 0
for age, survived in zip(df["Age"], df["Survived"]):
	if np.isnan(age) or np.isnan(survived):
		continue
	if survived == 1:
		survivors += 1
		survs_added_age += age
	else:
		deads += 1
		deads_added_age += age
survs_medium_age = survs_added_age / survivors
survs_medium_age = math.floor(survs_medium_age * 100) / 100
deads_medium_age = deads_added_age / deads
deads_medium_age = math.floor(deads_medium_age * 100) / 100

# Fill the holes from the column "Age".
length = len(df)
for i in range(0, length):
	if np.isnan(df["Age"][i]) == 0:
		continue
	if df["Survived"][i] == 0:
		df.loc[i, "Age"] = deads_medium_age
	if df["Survived"][i] == 1:
		df.loc[i, "Age"] = survs_medium_age

# Fill the holes from the column "Cabin" and "Embarked".
col_title = ["Cabin", "Embarked"]
for i in range(0, 2):
	# Split the dataset in 2:survivors and deads.
	curr_col_title = col_title[i]
	survivors = df.loc[(df["Survived"] == 1)]
	deads = df.loc[(df["Survived"] == 0)]
	categories = [survivors, deads]

	# Find the most frequent option for every category
	# and fill the holes from current column.
	for ctg in categories:
		# Options
		curr_col = ctg[curr_col_title]
		options = set(curr_col)
		dict_options = {}
		index = 0
		for option in options:
			if isinstance(option, str) and option not in dict_options.keys():
				dict_options[option] = index
				index += 1
		# Counters.
		cnt = np.full(len(options), 0)
		for elem in curr_col:
			if isinstance(elem, str) == 1:
				index = dict_options.get(elem)
				cnt[index] += 1
		# Most frequent option from current category.
		top_cnt = -1
		for option in options:
			if isinstance(option, str) == 0:
				continue
			index = dict_options[option]
			curr_cnt = cnt[index]
			if curr_cnt > top_cnt:
				top = option
				top_cnt = curr_cnt
		# Fill holes.
		length = len(df)
		for i in range(0, length):
			if isinstance(df[curr_col_title][i], str) == 1:
				continue
			if ctg.equals(survivors) and df["Survived"][i] == 1:
				df.loc[i, curr_col_title] = top
			if ctg.equals(deads) and df["Survived"][i] == 0:
				df.loc[i, curr_col_title] = top

# Save the ney dataframe.
df.to_csv("train_after_task_8.csv", index = "False")