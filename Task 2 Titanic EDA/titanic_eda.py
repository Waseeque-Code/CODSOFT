import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_titanic.csv')
print(f'Check few rows : {df.head(5)}')

# TITANIC EDA PROJECT

#1. Descriptive Statistics

print(f'Dataset Shape : {df.shape}')

print('\nDESCRIPTIVE STATISTIC')
print(df.describe())

print('\nMean, Median, Mode')
print('Age - Mean:', round(df['Age'].mean(), 2), '| Median :', df['Age'].median())
print('Fare - Mean:', round(df['Fare'].mean(), 2), '| Median :', round(df['Fare'].median(), 2))
print('Age - Mode:', df['Age'].mode()[0])

print('\nStandard Deviation & Variance')
print('Age std:', round(df['Age'].std(), 2), '| Var:', round(df['Age'].var(), 2))
print('Fare std:', round(df['Fare'].std(), 2), '| Var:', round(df['Fare'].var(), 2))

print('Skewness & Kurtosis')
print('Age Skew:', round(df['Age'].skew(), 2))
print('Fare Skew:', round(df['Fare'].skew(), 2))

#2. DISTRIBUTION (Histogram)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(df['Age'], bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')

axes[0, 1].hist(df['Fare'], bins=30, color='salmon', edgecolor='black')
axes[0, 1].set_title('Fare Distribution')
axes[0, 1].set_xlabel('Fare')

axes[1, 0].hist(df['Pclass'], bins=3, color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Passenger Class Distribution')
axes[1, 0].set_xlabel('Pclass')

axes[1, 1].hist(df['SibSp'], bins=8, color='plum', edgecolor='black')
axes[1, 1].set_title('Siblings/Spouses Distribution')
axes[1, 1].set_xlabel('SibSp')

plt.tight_layout()
plt.savefig('Distributions.png', dpi=100)
plt.show()

#3. Relationship

print('\nCorrelation Matrix')

numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()
print(corr)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('Correlations.png', dpi=100, bbox_inches='tight')
plt.show()

#4. Outlier Detection 
print('\nOutliers Detection')

for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    Lower = Q1 - 1.5*IQR
    Upper = Q3 + 1.5*IQR
    outliers = df[(df[col] < Lower) | (df[col] > Upper)]
    print(f'{col}: {len(outliers)} outliers (bounds: {Lower:.2f} to {Upper:.2f})')

#Boxplot

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].boxplot(df['Age'].dropna())
axes[0].set_title('Age Boxplot')
axes[1].boxplot(df['Fare'].dropna())
axes[1].set_title('Fare Boxplot')
plt.tight_layout()
plt.savefig('Boxplots.png', dpi=100)
plt.show()

# Business Quess
print('\nBusiness Questions')

survival_rate = df['Survived'].mean() * 100
print(f'Q1 : Overall survival rate : {survival_rate}')

print('\nSuvival by Gender')
print(df.groupby('Sex')['Survived'].mean() * 100)

print('\nSurvival by Passenger Class')
print(df.groupby('Pclass')['Survived'].mean() * 100)

print('\nAverage Age Class')
print(df.groupby('Pclass')['Age'].mean())

print(f'\nAverage Fare by Class')
print(df.groupby('Pclass')['Fare'].mean())

