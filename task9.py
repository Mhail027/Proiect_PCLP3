import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("*********** TASK 9 ***********")

# Read the data set.
df = pd.read_csv("../titanic/train.csv")

# Create a column with the title of persons.
df[['Surname', 'First name']]= df["Name"].str.split(',', expand = True)
df[['Title', 'Fm 1', 'Fm 2']] =df["First name"].str.split('.', expand = True)
df["Title"] = df["Title"].str.strip()


# Initialize the lists with the options of title after gender.
female_titles = ["Ms", "Mlle", "Mme", "Lady", "the Countess", "Miss", "Mrs"]
male_titles = ["Don", "Capt", "Major", "Master", "Rev", "Col", "Sir", "Mr"]
male_titles.append("Jonkheer")
neutral_titles = ["Dr"]

# Count the wrong and the right title
right_titles = 0
wrong_titles = 0
for i in range(0, len(df)):
	title = df["Title"][i]
	sex = df["Sex"][i]
	if not isinstance(title, str):
		continue
	if title in neutral_titles:
		right_titles += 1
		continue
	if not isinstance(sex, str):
		continue
	if sex == "male":
		if title in male_titles:
			right_titles += 1
		else:
			wrong_titles += 1
			print(f"#{title}#, {sex}")
	if sex == "female":
		if title in female_titles:
			right_titles += 1
		else:
			wrong_titles += 1

# Do a grphic with the wrong and right titles
w = wrong_titles
r = right_titles
plt.pie([w, r], labels = ["wrong gender", "right gender"], autopct = '%1.1f%%')
plt.title("The titles")
plt.show()
