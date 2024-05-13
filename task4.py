import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("*********** TASK 4 ***********")

# Read the data set.
df = pd.read_csv("../titanic/train.csv")

# Find the columns with holes.
columns = df.columns
holes_per_col = df.isnull().sum().tolist()
lines = len(df)
print("Columns with missing values")
i = 0
for col in columns:
	if holes_per_col[i] != 0:
		percentage = holes_per_col[i] / lines * 100
		percentage = math.floor(percentage * 100)/ 100
		print(f"{col}:  {holes_per_col[i]} values  -  {percentage}%")
	i += 1


# Find the numbers of missing values for the 2 classes
# from the column "Survived".
deads = df.loc[df["Survived"] == 0]
holes_list = deads.isnull().sum().tolist()
holes_deads = sum(holes_list)

survivors = df.loc[df["Survived"] == 1]
holes_list = survivors.isnull().sum().tolist()
holes_surv = sum(holes_list)

[lines, cols] = deads.shape
pct = holes_deads / (lines * cols)
pct = math.floor(pct * 100) / 100
print("")
print("Percentage of missing values for deads")
print(f"{pct} %")

[lines, cols] = survivors.shape
pct = holes_surv / (lines * cols)
pct = math.floor(pct * 100) / 100
print("Percentage of missing values for survivors")
print(f"{pct} %")