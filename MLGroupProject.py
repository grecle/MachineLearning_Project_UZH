import numpy as np
import pandas as pd

# read in the CSV file
file_path = "/Users/cleogreb/Desktop/GroupProjectDataSet.csv"
df = pd.read_csv(file_path)

# MSSubClass beheben mit dummy variabeln - Grund gleich behandeln wie die sektoren in ZH in der VL
df['MSSubClass'] = df['MSSubClass'].astype(str)
df['MSSubClass_cat'] = df['MSSubClass'].apply(lambda x: x.split('-')[0])
df = pd.concat([df, pd.get_dummies(df['MSSubClass_cat'], prefix='MSSubClass')],
               axis=1)
print(df['MSSubClass_50.0'].sum())

# MSZoning beheben mir dummy variabeln - Grund gleich behandeln wie die sektoren in ZH in der VL

df = pd.concat([df, pd.get_dummies(df['MSZoning'], prefix='MSZoning')], axis=1)
print(df['MSZoning_RM'].sum())

# Replace all LotFrontage nan values with 0 bc those nan should mean that the house is not adjacent to a street.
df['LotFrontage'].fillna(0, inplace=True)

# Replace the "Street" column to map the categories to integer values
df['Street'] = df['Street'].replace({'Grvl': 0, 'Pave': 1})
print((df['Street'] == 1).sum())

# Replace the "Alley" column to map the categories to integer values*df['Alley'] = df['Alley'].replace({df['Alley'].empty(): "None"})

print(5*"-")

#print((df['Alley'] == "None").sum())
print(5*"-")

missing_values_per_row = df.isnull().sum()
print(missing_values_per_row)
print(5*"-")
corr_coef = df['GarageYrBlt'].corr(df['YearBuilt'], method='pearson')
print(corr_coef)




print(df.head())


print(df["LotArea"].isnull().sum())
