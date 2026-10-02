import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

#Load dataset
df = pd.read_csv('Mall_Customers.csv')

#1. Data Inspection
print("===Dataset Shape===")
print(df.shape)

print("First 5 rows")
print(df.head())

print("===Info===")
print(df.info())

print("===Descriptive Statistics===")
print(df.describe())

print("===Missing Values===")
print(df.isnull().sum())

#2. Customer Segmentation by Age
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 25, 35, 50, 100],
                        labels=['Young', 'Adult', 'Middle-aged', 'Senior'])
print('\n==== Customer by Age Group ====')
print(df['AgeGroup'].value_counts())

age_income = df.groupby('AgeGroup')['Annual Income (k$)'].mean()
print('\n==== Average annual income by Age Group ====')
print(age_income)

#3. Segmentation by Gender
print('\n==== Gender Distribution ====')
print(df['Gender'].value_counts())

print('\n==== Average spending score by Gender ====')
print(df.groupby('Gender')['Spending Score (1-100)'].mean())

#4. Income vs Spending Score Analysis
print('\n==== Correlation between Income vs Spending Score ====')
print(df[['Annual Income (k$)', 'Spending Score (1-100)']].corr())

#5. Visualizations 
#Gender Distribution by Pie
plt.figure(figsize=(8, 6))
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, 
        autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff'],
        explode=(0.05, 0.05), shadow=True)
plt.title('Gender Distribution', fontsize=14, fontweight='bold')
plt.savefig('gender_distribution_pie.png', dpi=100, bbox_inches='tight')
plt.show()

# Age Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, color='#ff9999', edgecolor='black')
plt.title('Age Distribution of Customers', fontsize=14, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('Age_distribution_hist.png', dpi=100, bbox_inches='tight')
plt.show()

# Income vs Spending Score (Scatter)
plt.figure(figsize=(10, 6))
color = {'Male': '#3498db', 'Female': '#e74c3c'}
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    plt.scatter(subset['Annual Income (k$)'],
                subset['Spending Score (1-100)'],
                c=color[gender], label=gender, alpha=0.5,
                edgecolors='black', s=60)
plt.title('Annual Income vs Spending Score', fontsize=14, fontweight='bold')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig('Income_vs_spending_scatter.png', dpi=100, bbox_inches='tight')
plt.show()

# Average Spending by Age Group (Bar)
plt.figure(figsize=(10, 6))
age_spending = df.groupby('AgeGroup')['Spending Score (1-100)'].mean()
bars = plt.bar(age_spending.index, age_spending.values, 
               color=['#2ecc71', '#f39c12', '#e74c3c', '#9b59b6'],
               edgecolor='black')
plt.title('Average spending score by Age Group', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel("Avg Spending Score")
for i, v in enumerate(age_spending.values):
    plt.text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')
plt.savefig('Avg_spending_by_agegroup.png', dpi=100, bbox_inches='tight')
plt.show()

# Average Income by Gender
plt.figure(figsize=(8, 6))
gender_income = df.groupby('Gender')['Annual Income (k$)'].mean()
plt.bar(gender_income.index, gender_income.values, 
        color=['#3498db', '#e74c3c'], edgecolor='black')
plt.title('Average Annual Income by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Avg Annual Income')
for i, v in enumerate(gender_income.values):
    plt.text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')
plt.savefig('Avg_income_by_gender.png', dpi=100, bbox_inches='tight')
plt.show()

# Dashboard
#Gen pie
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Customer Segmentation Dashboard', fontsize=16, fontweight='bold')

axes[0, 0].pie(gender_counts.values, labels=gender_counts.index,
               autopct = '%1.1f%%', colors=['#e74c3c', '#3498db'],
               startangle=90)
axes[0, 0].set_title('Gender Distribution')

#Age hist
axes[0, 1].hist(df['Age'], bins=20, color='#e74c3c', edgecolor='black')
axes[0, 1].set_title('Age Distribution')
axes[0, 1].set_xlabel('Age')

#Inc vs Spend scatter
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    axes[1, 0].scatter(subset['Annual Income (k$)'],
                       subset['Spending Score (1-100)'],
                       c=color[gender] if gender == 'Male' else '#e74c3c',
                       label=gender, alpha=0.6, edgecolors='black', s=60)
axes[1, 0].set_title('Annual Income vs Spending Score')
axes[1, 0].set_xlabel('Annual Income (k$)')
axes[1, 0].set_ylabel('Spending Score (1-100)')
axes[1, 0].legend()

# Avg spending by age
axes[1, 1].bar(age_spending.index, age_spending.values, 
               color=['#23cc71', '#f39c12', '#e74c3c', '#9b59b6'],
               edgecolor='black')
axes[1, 1].set_title('Average Spending Score by Age Group')
axes[1, 1].set_ylabel('Avg Spending Score')

plt.tight_layout()
plt.savefig('Customer_Segmentation_Dashboard.png', dpi=100, bbox_inches='tight')
plt.show()

print('Task 4 Completed!!')