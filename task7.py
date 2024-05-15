import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("*********** TASK 7 ***********")

# Read the data set.
df = pd.read_csv("../titanic/train.csv")

# Find the number of children and adults
# which survived and died in every.
child_survs = 0
child_deads = 0
adult_survs = 0
adult_deads = 0
for age, survived in zip(df["Age"], df["Survived"]):
	if np.isnan(age) or np.isnan(survived):
		continue
	if age < 18 and survived == 1:
		child_survs += 1
	if age < 18 and survived == 0:
		child_deads += 1
	if age >= 18 and survived == 1:
		adult_survs += 1
	if age >= 18 and survived == 0:
		adult_deads += 1

# Find how the percentage of childs from
# the ship.
children = child_survs + child_deads
adults = adult_survs + adult_deads
persons =  children + adults
pct = children / persons
pct = math.floor(pct * 100) / 100
print(f"Percentage of children from ship: {pct}%")

# Do a graphic with the obtained informations.
fig, (pies) = plt.subplots(1, 2)
labels = ["D", "S"]
fig.suptitle("Rate of survival")

cnt = [child_deads, child_survs]
pies[0].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[0].set_title("Children")

cnt = [adult_deads, adult_survs]
pies[1].pie(cnt, labels = labels, autopct = '%1.1f%%')
pies[1].set_title("Adults")

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("*********** TASK 5 ***********")

# Read the data set.
df = pd.read_csv("../titanic/train.csv")

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