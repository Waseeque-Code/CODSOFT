# Task 5: Web Data Extraction & Analysis

## 🎯 Objective
Scrape data from a public website using BeautifulSoup, clean it, and perform exploratory analysis.

## 🌐 Website Scraped
**Books to Scrape** (http://books.toscrape.com/) — a practice website for web scraping.

## 🔍 Data Extracted
- Book Title
- Price (£)
- Rating (1-5 stars)
- Availability

**Total Books Scraped:** 100 (5 pages)

## 🛠️ Steps Performed

### 1. Web Scraping
- Used `requests` to fetch pages
- Used `BeautifulSoup` to parse HTML
- Extracted title, price, rating, availability
- Added 1-second delay between requests (ethical scraping)

### 2. Data Cleaning
- Removed duplicates
- Cleaned price column (removed £ symbol)
- Converted rating text to numbers (One=1, Five=5)
- Created `In_Stock` binary column

### 3. Exploratory Analysis
- Descriptive statistics (mean, median, std)
- Rating distribution
- Price distribution
- Average price by rating
- Price vs Rating correlation

## 📈 Visualizations
- Rating distribution (bar chart)
- Price distribution (histogram)
- Average price by rating (bar chart)
- Price vs Rating (scatter plot)
- Combined dashboard

## 💡 Key Insights
- Most books are rated 3-4 stars
- Price range: £10-£60
- No strong correlation between price and rating
- Most books are in stock

## 🎁 Bonus
- Automated scraping loop for 5 pages
- Exported data to `books_scraped.csv`

## 🛠️ Tools Used
Python, Requests, BeautifulSoup, Pandas, Matplotlib, Seaborn

## 📁 Files
- `task5.ipynb` — Full code
- `books_scraped.csv` — Scraped dataset
- All chart PNGs
- `dashboard_books.png` — Combined dashboard
