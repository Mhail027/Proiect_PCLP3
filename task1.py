import numpy as np
import pandas as pd
import itertools as it

'Read the information from a data set, put them into a list'
'and after return that list.'
def read_data(path):
	'Open the file.'
	f = open(path, "r")

	'Create a list of lists with the lines from file.'
	list = []
	for line in f:
		'Eliminate the new line character.'
		line = line[:-1]
		'Slpit the line on columns.'
		line = line.split(',')
		'A comma is in plus. We must reunite'
		'the fields from name.'
		new_line = []
		for elem in line:
			if len(elem) > 0:
				if elem[0] == '"':
					elem = elem[1:]
				if elem[len(elem) - 1] == '"':
					elem = elem[:-1]
					l = len(new_line)
					new_line[l - 1] = new_line[l - 1] + "," + elem
					continue 
			new_line.append(elem)
		'Add the line in the matrix.'
		list.append(new_line)

	'Close the file'
	f.close()

	'Return the list which contains the read information'
	return list

'Eliminate the duplicate lines.'
def eliminate_duplicates(list):
	new_list = []
	for line in list:
		if line not in new_list:
			new_list.append(line)
	return new_list

def print_types_of_columns(list):
	nr_cols = len(list[0])
	type = [""] * nr_cols

	for line in list[1:]:
		for i in range(nr_cols):
			elem = line[i]
			if (type[i] == "string"):
				continue
			if (elem.isdigit()):
				type[i] = "int"
			else:
				type[i] = "string"
	
	line = list[0]
	for i in range(nr_cols):
		print(f"{line[i]}: {type[i]}")

def print_holes_per_column(list):
	nr_cols = len(list[0])
	holes = np.full(( nr_cols), 0)

	for line in list[1:]:
		for i in range(nr_cols):
			elem = line[i]
			if len(elem) == 0:
				holes[i] += 1

	line = list[0]
	for i in range(nr_cols):
		print(f"{line[i]}: {holes[i]} holes")

print("*********** TASK 1 ***********")
list = read_data("../titanic/train.csv")
nr_lines = len(list)
nr_cols = len(list[0])
print(f"Number of lines: {nr_lines}")
print(f"Number of columns: {nr_cols}")
list = eliminate_duplicates(list)
if len(list) == nr_lines:
	print("Doesn't exist duplicate lines.")
else:
	print("Exists duplicate lines.")
print_types_of_columns(list)
print_holes_per_column(list)