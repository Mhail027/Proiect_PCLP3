import numpy as np
import matplotlib.pyplot as plt

# read_data() - Reads the information from a data set,
# put them into a list and after return that list.
#
# @param path: the path to the file in which is saved
#	the data set.
#
# @return - The list with the read information.
def read_data(path):
	# Open the file.
	f = open(path, "r")

	# Create a list of lists with the lines from file.
	list = []
	for line in f:
		# Eliminate the new line character.
		line = line[:-1]
		# Slpit the line on columns.
		line = line.split(',')
		# A comma is in plus. We must reunite the name.
		# In the same time, we give up at the quotation
		# marks from the name.
		new_line = []
		for elem in line:
			if len(elem) > 0:
				if elem[0] == '"':
					elem = elem[1:]
				if elem[len(elem) - 1] == '"':
					elem = elem[:-1]
					length = len(new_line)
					new_line[length - 1] = new_line[length - 1] + "," + elem
					continue 
			new_line.append(elem)
		# Add the line in list.
		list.append(new_line)

	# Close the file.
	f.close()
	# Return the created list.
	return list

# eliminate_duplicate() - Eliminate the duplicate elements
# from a list.
#
# @param list: the list with which we work
#
# @return - The list without duplicates.
def eliminate_duplicates(list):
	new_list = []
	for line in list:
		if line not in new_list:
			new_list.append(line)
	return new_list

# extract_column() - Create a list with the values from a
# column.
#
# @param list: the list with the columns
# @param col_name: the wanted column
#
# @return - The created list.
def extract_column(list, col_name):
	# Find the index of the wanted column.
	header = list[0]
	idx_col = -1
	for i in range(len(header)):
		if header[i] == col_name:
			idx_col = i
			break
	
	# Extract the column.
	col = []
	for line in list[1:]:
		col.append(line[idx_col])

	# Return the column.
	return col

# @brief: Counts the number of aparitions of
# every element from list_2 in the list_1.
def count_aparitions(list_1, list_2):
	counter = np.full((len(list_2)), 0)
	for elem in list_1:
		counter[list_2.index(elem)] += 1
	return counter

# @brief: Print a pie graphic with the given informations.
def print_pie_graphic(options, counters, title):
	plt.pie(counters, labels = options, startangle=90,
			shadow = True, autopct = '%1.1f%%')
	plt.title(title)
	plt.legend()
	plt.show()

		
