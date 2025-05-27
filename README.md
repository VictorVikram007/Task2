# Task 2: Exploratory Data Analysis (EDA) - Titanic Dataset 

##  Objective
To perform Exploratory Data Analysis (EDA) on the Titanic dataset using descriptive statistics and a wide variety of visualizations, including interactive plots with Plotly.

---

##  Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly

---

##  Files in This Repository

| File Name             | Description |
|-----------------------|-------------|
| `Titanic-Dataset.csv` |  Titanic dataset used for EDA from kaggle |
| `task2.py`            | Python script performing full EDA using all required tools |
| `task2-01.png` to `task2-11.png` | Screenshots of visual outputs from the script |
| `README.md`           | This file describing the project |

---

##  Steps Performed

1. **Loaded the Titanic dataset** using `pandas`.
2. **Handled missing values**:
   - Filled `Age` and `Fare` with median values.
   - Dropped `Cabin` due to excessive nulls.
   - Removed remaining null rows.
3. **Generated Summary Statistics**:
   - Dataset overview
   - `.describe()`, `.info()`, `.skew()`
4. **Created Static Visualizations** using `matplotlib` and `seaborn`:
   - Histograms of numeric features
   - Boxplots for Age vs Survived and Fare vs Pclass
   - Correlation heatmap
   - Pairplot of key features
5. **Created Interactive Visualizations** using `plotly`:
   - Histogram of Age
   - Boxplot of Age by Survival
   - Interactive correlation heatmap
   - Scatterplot of Age vs Fare colored by Survived

---

##  Visualizations Captured

| Screenshot | Description |
|------------|-------------|
| `task2-01.png` | Dataframe `.head()` output |
| `task2-02.png` | Histogram of numeric features |
| `task2-03.png` | Seaborn boxplot: Age vs Survived |
| `task2-04.png` | Seaborn boxplot: Fare vs Pclass |
| `task2-05.png` | Seaborn heatmap of correlation matrix |
| `task2-06.png` | Pairplot of Age, Fare, Pclass, and Survived |
| `task2-07.png` | Plotly histogram: Age Distribution |
| `task2-08.png` | Plotly boxplot: Age by Survival |
| `task2-09.png` | Plotly correlation heatmap |
| `task2-10.png` | Plotly scatterplot: Fare vs Age colored by Survived |
| `task2-11.png` | Skewness output |

---

##  Key Insights

- **Class Impact**: Higher-class passengers had higher survival rates.
- **Age Distribution**: Younger passengers had higher survival probability.
- **Fare**: Skewed with a few high-value outliers; also influenced survival.
- **Multicollinearity**: Moderate correlations between `Fare`, `Pclass`, and `Survived`.
- **Visual Trends**: Patterns clearly visible through both static and interactive charts.

---
