import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('train.csv')
print(f'First 5 rows : \n{df.head(5)}')
print(df.info())

# Check null values
print(f'Total Missing values in all column \n{df.isnull().sum()}')

#Duplicate rows
print(f'Duplicate rows :\n{df.duplicated().sum()}')

#Types
print(f'Data types :\n{df.dtypes}')

# Age (Handle missing value)
df['Age'] = df['Age'].fillna(df['Age'].median())
print(f'After cleaning missing values :\n{df['Age'].isnull().sum()}')

# Drop Cabin column becuase 77% data is missing !!
df = df.drop(columns=['Cabin'])
print('Cabin drop successfully')

# Embarked
print(f'Sample :\n{df['Embarked'].sample(10)}')
print(df['Embarked'].value_counts())

#fill with mode()
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(f'After filling :{df["Embarked"].isnull().sum()}')
print(f'Now! :\n{df['Embarked'].value_counts()}')

# Verifing
print(df.isnull().sum())
print(f'Shape :{df.shape}')

#Sex encoding (male : 0 and female : 1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
print(f'After encoding :{df['Sex'].value_counts()}')

df.to_csv('Cleaned_titanic.csv', index=False)
print('Cleaned dataset saved')