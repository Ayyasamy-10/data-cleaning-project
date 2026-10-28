
import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kumar", "Priya", "Divya"],
    "Age": [22, 25, None, 25, 23],
    "City": ["Chennai", "Madurai", "Salem", "Madurai", "Coimbatore"],
    "Salary": [20000, 25000, 22000, 25000, None]
}

df = pd.DataFrame(data)

print("BEFORE CLEANING")
print(df)

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\nAFTER CLEANING")
print(df)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
