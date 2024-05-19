import numpy as np
import pandas as pd

print("*********** TASK 1 ***********")

# Read the data set.
df = pd.read_csv("train.csv")

# Find the number of lines and of columns.
[nr_lines, nr_cols] = df.shape
print(f"Number of lines: {nr_lines}")
print(f"Number of columns: {nr_cols}")

# Verify if exists duplicates.
print("")
dups = df.duplicated()
if True in dups:
	print("Exists duplicates.")
else:
	print("Doesn't exist duplicates.")

# Find the type of the elements from every column.
print("")
print("Column           Type")
print(df.dtypes)

# Find the number of holes from every column.
print("")
print("Column     Missing values")
columns = df.columns
a = df.isnull().sum()
print(a)