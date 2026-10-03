# CodSoft Data Analytics Internship

## 📋 Internship Details

| Field | Details |
|-------|---------|
| **Intern Name** | Waseeque Ahmad |
| **Domain** | Data Analytics |
| **Internship Duration** | 15 Sept 2026 – 15 Oct 2026 |
| **Offer Letter Issue Date** | 13 Sept 2026 |
| **Batch Number** | SEPT BATCH C24 |

---

## 📌 About

This repository contains all the tasks completed during my **Data Analytics Virtual Internship** at **CodSoft**.

---

## 📁 Tasks

### ✅ Task 1: Data Cleaning and Preprocessing

**Objective:** Clean and prepare a raw dataset for further analysis using Pandas.

**Dataset:** Titanic Dataset (891 rows × 12 columns)

**Steps Performed:**
- Imported dataset using Pandas and inspected structure (`head()`, `info()`, `shape`)
- Identified missing values:
  - `Age` → 177 missing
  - `Cabin` → 687 missing
  - `Embarked` → 2 missing
- Handled missing values:
  - `Age` → filled with median (robust to outliers)
  - `Embarked` → filled with mode
  - `Cabin` → dropped (77% missing, not useful)
- Checked and removed duplicate rows (0 found)
- Corrected data types and stripped extra spaces from text columns
- Encoded categorical column (`Sex`) for analysis
- Saved cleaned dataset as `cleaned_titanic.csv`

**Files:** `Task1_Data_Cleaning/`

---

### ✅ Task 2: Exploratory Data Analysis (EDA)

**Objective:** Analyze the cleaned dataset using descriptive statistics, identify trends, distributions, relationships, and detect outliers.

**Dataset:** Titanic Dataset (cleaned in Task 1) — 891 rows × 11 columns

**Steps Performed:**
- Generated descriptive statistics (mean, median, mode, std, variance, skewness)
- Visualized distributions using histograms (Age, Fare, Pclass, SibSp)
- Created a correlation heatmap to find relationships between variables
- Detected outliers using the IQR method
- Answered key business questions using summary statistics

**Key Findings:**
- Overall survival rate: **38.38%**
- Female survival: **74.20%** vs Male survival: **18.89%**
- 1st class survival: **62.96%** vs 3rd class: **24.24%**
- Strongest correlations: `Sex ↔ Survived` (+0.543), `Fare ↔ Pclass` (−0.549)
- Outliers: Age (66), Fare (116) — kept as valid data points

**Files:** `Task2_EDA/`

---

### ✅ Task 3: Data Visualization Dashboard

**Objective:** Create meaningful visualizations to present insights from the Titanic dataset.

**Dataset:** Titanic Dataset (cleaned in Task 1)

**Visualizations Created:**
- Bar charts: Survival by Gender and Passenger Class
- Pie chart: Overall survival distribution
- Line chart: Survival by Age Group
- Scatter plot: Age vs Fare (colored by survival)
- Histogram: Age distribution by survival
- Heatmap: Correlation matrix
- Combined dashboard: 4-in-1 view

**Key Insights:**
- Female survival (74.2%) >> Male survival (18.9%)
- 1st class survival (63%) >> 3rd class (24.2%)
- Higher fare correlates with better survival

**Files:** `Task3_Visualization/`

---

### ✅ Task 4: Customer Data Analysis

**Objective:** Analyze customer purchasing behavior and segment customers to identify valuable groups.

**Dataset:** Mall Customer Segmentation Dataset (200 customers)

**Steps Performed:**
- Inspected data structure and descriptive statistics
- Segmented customers by age, gender, and income
- Analyzed income vs spending relationships
- Created visual reports (pie, histogram, scatter, bar charts)
- Built a combined dashboard

**Key Insights:**
- Female customers are the majority
- High income + high spending = most valuable group
- Age groups show different spending patterns

**Files:** `Task4_Customer_Analysis/`

---

### ✅ Task 5: Web Data Extraction & Analysis

**Objective:** Scrape data from a public website using BeautifulSoup and perform exploratory analysis.

**Dataset:** Books to Scrape (http://books.toscrape.com/) — 100 books from 5 pages

**Steps Performed:**
- Scraped book details (Title, Price, Rating, Availability) using Requests and BeautifulSoup
- Added 1-second delay between requests for ethical scraping
- Cleaned data by removing duplicates and fixing data types
- Converted rating text to numbers (One=1 to Five=5)
- Performed exploratory analysis on price, rating, and availability
- Created visual reports (bar, histogram, scatter charts)
- Built a combined dashboard
- Exported scraped data to `books_scraped.csv`

**Key Insights:**
- Most books are rated 3-4 stars
- Price range: £10 to £60
- No strong correlation between price and rating
- Most books are in stock

**Files:** `Task5_Web_Scraping/`

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- VS Code

---

## 🔗 Connect

- **LinkedIn:** [CodSoft](https://www.linkedin.com/company/codsoft/)
- **Website:** https://www.codsoft.in

---

⭐ *This repository is maintained as part of the CodSoft Internship Program.*
