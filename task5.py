import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("**** TASK 5 ****")

# Read the data set.
df = pd.read_csv("train.csv")

# Create the list for the new column.
# (Category of age)
idxs = [] 
for age in df["Age"]:
	if np.isnan(age):
		idxs.append(np.nan)
		continue
	if 0 <= age and age < 21:
		idxs.append(0)
	if 21 <= age and age < 41:
		idxs.append(1)
	if 41 <= age and age < 61:
		idxs.append(2)
	if age >= 61:
		idxs.append(3)
# Add the column.
df.insert(12, "Category of age", idxs)

# Find the numbers of person from every
# category of age.
cnt = np.full(4, 0)
for category in df["Category of age"]:
	if np.isnan(category):
		continue
	cnt[int(category)] += 1

# Create a graphic for the column "Category of age".
plt.bar(["[0, 21)", "[21, 41)", "[41, 61)", ">= 61"], cnt)
for i in range(len(cnt)):
	plt.text(i, cnt[i], str(cnt[i]), ha = 'center', va = "bottom")
plt.xlabel("Category of age")
plt.ylabel("Persons")
plt.show()

# Save the ney dataframe.
df.to_csv("train_after_task_5.csv", index = "False")