import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("**** TASK 6 ****")

# Read the data set.
df = pd.read_csv("train_after_task_5.csv")

# Find the number of men which survived
# and in every category of age.
survs = np.full(4, 0)
deads = np.full(4, 0)
men = df.loc[(df["Sex"] == "male")]
for cage, survived in zip(men["Category of age"], men["Survived"]):
	if np.isnan(cage) or np.isnan(survived):
		continue
	if survived == 1:
		survs[int(cage)] += 1
	else:
		deads[int(cage)] += 1

# Print the number of male survivors from category of age.
print("Male survivors")
print(f"[0, 21) years: {survs[0]}")
print(f"[21, 41) years: {survs[1]}")
print(f"[41, 61) years: {survs[2]}")
print(f">= 61 years: {survs[3]}")

# Do a graphic with the procents of male which survived and died
# from every category of age
# Create a graphic with the processed columns.
fig, (pies) = plt.subplots(2, 2)
labels = ["D", "S"]
fig.suptitle("Men")

cnt = [deads[0], survs[0]]
pies[0, 0].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[0, 0].set_title("[0, 21) years")

cnt = [deads[1], survs[1]]
pies[0, 1].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[0, 1].set_title("[21, 41) years")

cnt = [deads[2], survs[2]]
pies[1, 0].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[1, 0].set_title("[41, 61) years")

cnt = [deads[3], survs[3]]
pies[1, 1].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[1, 1].set_title(">= 61 years")

plt.show()

# Other graphic

#labels = ["[0, 21) D", "[0, 21) S", "[21, 41) D", "[21, 41) S", 
#		  "[41, 61] D", "[41, 61] S", ">= 61 D", ">=61 S"]
#cnt = [deads[0], survs[0], deads[1], survs[1], deads[2], survs[2],
#	   deads[3], survs[3]]	   
#plt.pie(cnt, labels = labels, autopct = '%1.1f%%')
#plt.show()