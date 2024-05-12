import numpy as np
import pandas as pd
import data_set as ds

# print_type_of_columns() - Prints of which
# type are the elements from every column.
# 
# @param list: list of lists in which every
#	list contains the fields from a line
def print_type_of_columns(list):
	# Create the vector of types.
	nr_cols = len(list[0])
	types = [""] * nr_cols

	# Find the type of elements from every
	# column.
	for line in list[1:]:
		for i in range(nr_cols):
			elem = line[i]
			if (type[i] == "string"):
				continue
			if (elem.isdigit()):
				type[i] = "int"
			else:
				type[i] = "string"
	
	# Print the result.
	line = list[0]
	for i in range(nr_cols):
		print(f"{line[i]}: {type[i]}")

# print_holed_per_column() - Prints the number
# of missing values from every column.
# 
# @param list: list of lists in which every
#	list contains the fields from a line
def print_holes_per_column(list):
	# Create the vector of holes.
	nr_cols = len(list[0])
	holes = np.full(( nr_cols), 0)

	# Find the number of holes from every
	# column.
	for line in list[1:]:
		for i in range(nr_cols):
			elem = line[i]
			if len(elem) == 0:
				holes[i] += 1

	# Print the result.
	line = list[0]
	for i in range(nr_cols):
		print(f"{line[i]}: {holes[i]} holes")


print("*********** TASK 1 ***********")

list = ds.read_data("../titanic/train.csv")
nr_lines = len(list)
nr_cols = len(list[0])
print(f"Number of lines: {nr_lines}")
print(f"Number of columns: {nr_cols}")

list = ds.eliminate_duplicates(list)
if len(list) == nr_lines:
	print("Doesn't exist duplicate lines.")
else:
	print("Exists duplicate lines.")

print_types_of_columns(list)
print_holes_per_column(list)