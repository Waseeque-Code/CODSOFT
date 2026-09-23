# Task 2: Exploratory Data Analysis (EDA)

## 📊 Dataset
Titanic Dataset (cleaned in Task 1) — 891 rows × 11 columns

## 🎯 Objective
Analyze the dataset using descriptive statistics, identify trends, distributions, relationships, and detect outliers.

---

## 📈 Descriptive Statistics

| Metric | Age | Fare |
|--------|-----|------|
| Mean | 29.36 | 32.20 |
| Median | 28.00 | 14.45 |
| Std Dev | 13.02 | 49.69 |
| Variance | 169.51 | 2469.44 |
| Skewness | 0.51 | 4.79 |

**Insight:** Fare is heavily right-skewed (4.79), meaning a few passengers paid very high fares.

---

## 📉 Distributions
- **Age:** Roughly normal, peak around 20–40 years
- **Fare:** Right-skewed, most tickets under £30
- **Pclass:** 3rd class is the largest group (491 passengers)
- **SibSp:** Most passengers travelled alone (0 siblings/spouses)

---

## 🔗 Correlations

| Relationship | Correlation | Meaning |
|--------------|-------------|---------|
| Sex ↔ Survived | **+0.543** | Females survived more |
| Pclass ↔ Survived | **-0.338** | Higher class = higher survival |
| Fare ↔ Pclass | **-0.549** | Higher class = higher fare |
| Parch ↔ SibSp | **+0.415** | Families travelled together |

---

## 🚨 Outlier Detection (IQR Method)

| Column | Outliers | Bounds |
|--------|----------|--------|
| Age | 66 | 2.50 to 54.50 |
| Fare | 116 | -26.72 to 65.63 |

**Insight:** Outliers are valid (wealthy passengers, children, elderly) — not removed.

---

## 💼 Business Questions Answered

### Q1: What is the overall survival rate?
**38.38%**

### Q2: Did gender affect survival?
| Gender | Survival Rate |
|--------|---------------|
| Female | **74.20%** |
| Male | **18.89%** |

### Q3: Did passenger class affect survival?
| Class | Survival Rate |
|-------|---------------|
| 1st | **62.96%** |
| 2nd | 47.28% |
| 3rd | 24.24% |

### Q4: Average age by class?
| Class | Avg Age |
|-------|---------|
| 1st | 36.81 |
| 2nd | 29.77 |
| 3rd | 25.93 |

### Q5: Average fare by class?
| Class | Avg Fare |
|-------|----------|
| 1st | £84.15 |
| 2nd | £20.66 |
| 3rd | £13.68 |

---

## ✅ Conclusion
- **Gender** and **passenger class** are the strongest predictors of survival
- Females and 1st class passengers had significantly higher survival rates
- Fare is highly skewed with valid outliers (wealthy passengers)
- Age distribution is roughly normal with children and elderly as outliers

---

## 🛠️ Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, VS Code

## 📁 Files
- `task2.ipynb` — Full analysis code
- `Distributions.png` — Histograms
- `Correlations.png` — Heatmap
