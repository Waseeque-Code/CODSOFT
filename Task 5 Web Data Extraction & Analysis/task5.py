import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

sns.set_style('whitegrid')

#1. Web Scraping
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

books = []

for page in range(1, 6):
    url = base_url.format(page)
    print(f"Scraping page {page}: {url}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for book in soup.find_all('article', class_='product_pod'):
        # Title
        title = book.h3.a['title']
        
        # Price
        price = book.find('p', class_='price_color').text
        price = float(price.replace('£', '').replace('Â', ''))
        
        # Rating
        rating_class = book.find('p', class_='star-rating')['class'][1]
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_map.get(rating_class, 0)
        
        # Availability
        availability = book.find('p', class_='instock availability').text.strip()
        
        books.append({
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Availability': availability
        })
    
    time.sleep(1)  

df = pd.DataFrame(books)
print(f"\nScraped {len(df)} books")
print(df.head())

#2. Data Cleaning
print('===Data Inf0===')
print(df.info())

print('\n===Missing Value===')
print(df.isnull().sum())

print('\n===Duplicates===')
print(df.duplicated().sum())

#Clean Availability
df['In_Stock'] = df['Availability'].apply(lambda x: 1 if 'In stock' in x else 0)

#3. Exploratory Analysis
print('===Descriptive Statistics===')
print(df.describe())

print('\n===Price by Rating===')
print(df.groupby('Rating')['Price'].mean().round(2))

print('===Rating Distribution===')
print(df['Rating'].value_counts().sort_index())

print('\n===Correlation===')
print(df[['Price', 'Rating']].corr())

#4. Visualization

#Rating distribution
plt.figure(figsize=(8, 5))
rating_counts = df['Rating'].value_counts().sort_index()
bars = plt.bar(rating_counts.index, rating_counts.values,
               color=['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#27ae60'],
               edgecolor = 'black')
plt.title('Book Rating Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Rating (Stars)')
plt.ylabel('Number of Books')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')
plt.savefig('rating_distribution.png', dpi=100, bbox_inches='tight')
plt.show()

#Price Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=30, color='green', edgecolor='black')
plt.title('Book Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price')
plt.ylabel('Number of Books')
plt.savefig('price_dist.png', dpi=100, bbox_inches='tight')
plt.show()

#Average Price by Rating
plt.figure(figsize=(8, 5))
avg_price = df.groupby('Rating')['Price'].mean()
bars = plt.bar(avg_price.index, avg_price.values,
               color='#9b59b6', edgecolor='black')
plt.title('Average Price by Rating', fontsize=14, fontweight='bold')
plt.xlabel('Rating (Stars)')
plt.ylabel('Average Price')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
plt.savefig('Avg_price_by_rating.png', dpi=100, bbox_inches='tight')
plt.show()

#Price vs Rating Scatter
plt.figure(figsize=(10, 6))
plt.scatter(df['Rating'], df['Price'], alpha=0.5,
            c='#3498db', edgecolors='black', s=60)
plt.title('Price vs Rating', fontsize=14, fontweight='bold')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.savefig('Scatter_price_rating.png', dpi=100, bbox_inches='tight')
plt.show()

#Dashbaord
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Books Scraping Analysis Dashboard', fontsize=18, fontweight='bold')

axes[0, 0].bar(rating_counts.index, rating_counts.values,
               color=['#e74c3c', '#e67e22', '#f1c40f', '#27ae60'],
               edgecolor='black')
axes[0, 0].set_title('Rating Distribution')
axes[0, 0].set_xlabel('Rating')

axes[0, 1].hist(df['Price'], bins=30, color='green', edgecolor='black')
axes[0, 1].set_title('Price Distribution')
axes[0, 1].set_xlabel('Price')

axes[1, 0].bar(avg_price.index, avg_price.values,
               color='#9b59b6', edgecolor='black')
axes[1, 0].set_title('Avg Price by Rating')
axes[1, 0].set_xlabel('Rating')

axes[1, 1].scatter(df['Rating'], df['Price'], alpha=0.5,
                   c='#3498db', edgecolor='black')
axes[1, 1].set_title('Price vs Rating')
axes[1, 1].set_xlabel('Rating')
axes[1, 1].set_ylabel('Price')

plt.tight_layout()
plt.savefig('Dashboard.png', dpi=100, bbox_inches='tight')
plt.show()

#Export to csv
df.to_csv('Book_scraped.csv', index=False)
print("Data saved to 'Book_scraped.csv'")
