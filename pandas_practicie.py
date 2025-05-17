import pandas as pd
import numpy as np

#Pandas has two main data structures:
#Series**: One-dimensional labeled array.
#DataFrame**: Two-dimensional, size-mutable, and labeled.

### **Series Example**
data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data)

### **DataFrame Example**
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

## **3️⃣ Reading Data**
# Reading from a CSV
df = pd.read_csv('data.csv')

# Reading from Excel
#df = pd.read_excel('data.xlsx')

print(df.head())        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.info())        # Summary of the DataFrame
print(df.describe())    # Statistical summary

## **5️⃣ Data Manipulation**
# Adding a column
df['Salary'] = [50000, 60000, 70000]

# Renaming columns
df.rename(columns={'Name': 'Full Name'}, inplace=True)

# Dropping a column
df.drop(columns=['City'], inplace=True)

##inplace=Ture -> original data is modifying (no copy created)

## **6️⃣ Filtering and Selection**
# Selecting columns
print(df[['Full Name', 'Age']])

# Conditional filtering
print(df[df['Age'] > 25])

## **7️⃣ Grouping and Aggregation**
grouped = df.groupby('Age').mean(numeric_only=True)
print(grouped)

## **8️⃣ Merging and Joining**
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Salary': [70000, 80000]})
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)

## **9️⃣ Handling Missing Data**
df.fillna(0, inplace=True)     # Replace NaN with 0
df.dropna(inplace=True)        # Drop rows with NaN

# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', index=False)


## **🔄 Visualization with Pandas**
import matplotlib.pyplot as plt

# Line Plot
df.plot(kind='line')
plt.show()