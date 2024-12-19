import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

# Load the data
data = pd.read_csv('data/train.csv')

# Stratified split
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
for train_indices, test_indices in split.split(data, data["Survived"]):  # Use "Survived" for stratification
    strat_train_set = data.loc[train_indices]
    strat_test_set = data.loc[test_indices]

# Plot histograms
plt.figure(figsize=(12, 6))

# Training set histograms
plt.subplot(1, 2, 1)
strat_train_set['Survived'].hist(alpha=0.7, label="Survived", color="blue")
strat_train_set['Pclass'].hist(alpha=0.7, label="Pclass", color="green")
plt.title("Training Set")
plt.legend()

# Test set histograms
plt.subplot(1, 2, 2)
strat_test_set['Survived'].hist(alpha=0.7, label="Survived", color="blue")
strat_test_set['Pclass'].hist(alpha=0.7, label="Pclass", color="green")
plt.title("Test Set")
plt.legend()

plt.show()




#data['Survived'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='coolwarm', legend=True)

# # Customize the pie chart
# plt.title("Survival Distribution")
# plt.ylabel("")  # Hide the ylabel for a cleaner look
# plt.show()

#print(data[['Sex', 'Survived']].groupby('Sex')['Survived'].mean())


# xpoints = np.random.randint(10, 1000, size=20)
# ypoints = np.random.randint(10, 100, size=20)

# plt.plot(xpoints, ypoints, 'r')
# plt.show()
