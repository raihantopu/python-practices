import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

data = pd.read_csv('titanic.csv')
# data['Survived'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='coolwarm', legend=True)

# # Customize the pie chart
# plt.title("Survival Distribution")
# plt.ylabel("")  # Hide the ylabel for a cleaner look
# plt.show()

print(data[['Sex', 'Survived']].groupby('Sex')['Survived'].mean())


# xpoints = np.random.randint(10, 1000, size=20)
# ypoints = np.random.randint(10, 100, size=20)

# plt.plot(xpoints, ypoints, 'r')
# plt.show()
