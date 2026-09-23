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

### ⏳ Task 3: [Coming Soon]

---

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
