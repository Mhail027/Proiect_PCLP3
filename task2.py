import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("*********** TASK 2 ***********")

# Read the data set.
df = pd.read_csv("../titanic/train.csv")

# Process the column "Survived".
surv = df["Survived"]
surv_options = set(surv)
surv_counters = np.full(len(surv_options), 0)
for elem in surv:
	surv_counters[elem] += 1

# Process the column "Pclass".
pclass = df["Pclass"]
pclass_options = set(pclass)
pclass_counters = np.full(len(pclass_options) + 1, 0)
for elem in pclass:
	pclass_counters[elem] += 1

# Process the column "Sex".
sex = df["Sex"]
sex_options = set(sex)
sex_counters = np.full(len(sex_options), 0)
for elem in sex:
	if elem == "male":
		sex_counters[0] += 1
	else:
		sex_counters[1] += 1

# Create a graphic with the processed columns.
fig, (surv_graphic, pclass_graphic, sex_graphic) = plt.subplots(1, 3)

surv_graphic.pie(surv_counters, labels = surv_options, autopct = '%1.1f%%')
surv_graphic.set_title("Survived")
pclass_graphic.pie(pclass_counters[1:4], labels = pclass_options,
				   autopct = '%1.1f%%')
pclass_graphic.set_title("Pclass")
sex_graphic.pie(sex_counters, labels = sex_options, autopct = '%1.1f%%')
sex_graphic.set_title("Sex")

plt.show()