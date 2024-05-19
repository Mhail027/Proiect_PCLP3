import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

print("*********** TASK 10 ***********")

# Read the data set.
df = pd.read_csv("train.csv")

# Select first 100 persons.
df = df.head(100)

# Keep just the columns "Fare", "Pclass" and "Survived"
df = df[["Fare", "Pclass", "Survived"]]

# Do the graphic.
sb.catplot(x = "Pclass", y = "Fare", hue = "Survived", data = df,
kind = "swarm", s = 5.5)
plt.show()