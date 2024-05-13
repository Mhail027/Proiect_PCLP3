import data_set as ds
import matplotlib.pyplot as plt
import math as m
import numpy as np

print("*********** TASK 3 ***********")

# Read the data set.
list = ds.read_data("../titanic/train.csv")
list = ds.eliminate_duplicates(list)

# Create the vector of types.
nr_cols = len(list[0])
types = [""] * nr_cols

# Find the type of elements from every
# column.
for line in list[1:]:
	for i in range(nr_cols):
		elem = line[i]
		if (types[i] == "string"):
			continue
		if elem.isdigit():
			types[i] = "int"
		else:
			types[i] = "string"

c = 0
for elem in types:
	if elem == "int":
		c += 1

fig, (col) = plt.subplots(1, c)
i = -1
i_plt = -1
for col_title in list[0]:
	i += 1
	if types[i] == "string":
		continue
	i_plt += 1
	column = ds.extract_column(list, col_title)
	options = ds.eliminate_duplicates(column)
	counter = ds.count_aparitions(column, options)

	col[i_plt].hist(options, len(options), color = "red", weights = counter)
	col[i_plt].set_title(col_title)

plt.show()