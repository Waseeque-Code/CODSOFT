# Task 1: Data Cleaning and Preprocessing

## 🎯 Objective
Clean and prepare a raw dataset for further analysis using Pandas.

## 📊 Dataset
**Titanic Dataset** — 891 rows × 12 columns

## 🔍 Problems Identified

| Column | Issue |
|--------|-------|
| Age | 177 missing values |
| Cabin | 687 missing values (77%) |
| Embarked | 2 missing values |
| — | 0 duplicate rows |

## 🛠️ Steps Performed

1. **Imported** the dataset using Pandas and inspected its structure (`head()`, `info()`, `shape`)
2. **Identified** missing values, duplicates, and data types
3. **Handled missing values:**
   - `Age` → filled with **median** (robust to outliers)
   - `Embarked` → filled with **mode**
   - `Cabin` → **dropped** (too many missing values)
4. **Removed duplicates** (none found)
5. **Stripped extra spaces** from text columns
6. **Verified** data types and consistency
7. **Saved** the cleaned dataset as `cleaned_titanic.csv`

## 📁 Files

| File | Description |
|------|-------------|
| `task1.py` |  full code |
| `cleaned_titanic.csv` | Final cleaned dataset |

## 🛠️ Tools Used
- Python
- Pandas
- VS Code

## ✅ Outcome
A clean, analysis-ready dataset with no missing values or duplicates.
