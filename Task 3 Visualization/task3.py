import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Style 
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 8)

#Load
df = pd.read_csv('cleaned_titanic.csv')

#Bar chart Survival vs Gender
survival_gender = df.groupby('Sex')['Survived'].mean()*100
plt.figure(figsize=(8, 5))
bar = plt.bar(['Male', 'Female'], survival_gender.values,
              color=['#3498db', '#e74c3c'], edgecolor='black')
plt.title('Survival Rate by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Survival Rate (%)')
plt.legend(bar, ['Male', 'Female'], loc='upper left')
for i, v in enumerate(survival_gender.values):
    plt.text(i, v+1, f'{v:.1f}%', ha='center', fontweight='bold')
plt.savefig('Bar_survival_gender.png', dpi=100, bbox_inches='tight')
plt.show()

#Bar chart : Survival by Class
survival_class = df.groupby('Pclass')['Survived'].mean()*100
plt.figure(figsize=(8, 5))

bars = plt.bar(['1st Class', '2nd Class', '3rd Class'], survival_class.values,
               color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black')
plt.title('Survival Rate by Passenger Class', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate (%)')
plt.legend(bars, ['1st Class', '2nd Class', '3rd Class'], loc='upper right')
for i, v in enumerate(survival_class.values):
    plt.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')
plt.savefig('Bar_surivival_class.png', dpi=100, bbox_inches='tight')
plt.show()

# Pie Chart : Overall Survival
survival_counts = df['Survived'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(survival_counts.values, labels=['Died', 'Survived'],
        autopct='%1.1f%%', colors=['#e74c3c', '#2ecc71'], 
        startangle=90, explode=(0.05, 0.05), shadow=True)
plt.title('Overall Survival Distribution', fontsize=14, fontweight='bold')
plt.savefig('Pie_survival_dist.png', dpi=100, bbox_inches='tight')
plt.show()

# Line Chart : Survival by Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 30, 50, 80],
                        labels=['Child', 'Teenager', 'Young', 'Adult', 'Senior'])
age_survival = df.groupby('AgeGroup')['Survived'].mean()*100
plt.figure(figsize=(10, 5))
plt.plot(age_survival.index, age_survival.values, marker='o',
         color='#9b59b6', linewidth=2, markersize=10)
plt.title('Survival Rate by Age Group', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate (%)')
plt.grid(True, alpha=0.3)
for i, v in enumerate(age_survival.values):
    plt.text(i, v + 2, f'{v:.1f}%', ha='center', fontweight='bold')
plt.savefig('Line_survival_agegroup.png', dpi=100, bbox_inches='tight')
plt.show()

# Scatter Plot : Age vs Fare
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Age'], df['Fare'], c=df['Survived'],
                      cmap='RdYlGn', alpha=0.6, edgecolor='black', s=50)
plt.title('Age vs Fare (colored by Survival)', fontsize=14, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.colorbar(scatter, label='Survived (0=No, 1=Yes)')
plt.savefig('scatter_age_fare.png', dpi=100, bbox_inches='tight')
plt.show()

# Histogram : Age distribution by Survival
plt.figure(figsize=(10, 6))
plt.hist([df[df['Survived']==0]['Age'], df[df['Survived']==1]['Age']],
          bins=20, label=['Died', 'Survived'], 
          color=['#e74c3c', '#2ecc71'], edgecolor='black')
plt.title('Age Distribution by Survival', fontsize=14, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.savefig('hist_age_survival.png', dpi=100, bbox_inches='tight')
plt.show()

# Headmap : Correlation
plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f',
            linewidths=0.5, square=True)
plt.title('Correlation Heatmap', fontsize=14, fontweight='bold')
plt.savefig('Heatmap_corr.png', dpi=100, bbox_inches='tight')
plt.show()

#Dashbaord
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Titanic Data Analysis Dashboard', fontsize=16, fontweight='bold')

#Top left : Survival by gender
axes[0, 0].bar(['Male', 'Female'], survival_gender.values,
               color=['#3498db', '#e74c3c'], edgecolor='black')
axes[0, 0].set_title('Survival by Gender')
axes[0, 0].set_ylabel('Survival Rate (%)')

#Top right : Survival by Class
axes[0,1].bar(['1st', '2nd', '3rd'], survival_class.values,
              color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black')
axes[0,1].set_title('Survival by Class')
axes[0,1].set_ylabel('Survival Rate (%)')

# Bottom-left: Age Distribution
axes[1,0].hist(df['Age'], bins=30, color='skyblue', edgecolor='black')
axes[1,0].set_title('Age Distribution')
axes[1,0].set_xlabel('Age')

# Bottom-right: Fare Distribution
axes[1,1].hist(df['Fare'], bins=30, color='salmon', edgecolor='black')
axes[1,1].set_title('Fare Distribution')
axes[1,1].set_xlabel('Fare')

plt.tight_layout()
plt.savefig('dashboard.png', dpi=100, bbox_inches='tight')
plt.show()

print('All visualizations created!')
