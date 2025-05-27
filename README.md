# Task 2: Exploratory Data Analysis (EDA) - Titanic Dataset 🚢

##  Objective
To perform Exploratory Data Analysis (EDA) on the Titanic dataset using statistics and visualizations to understand patterns, trends, and relationships in the data.

---

##  Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

---

##  Files in This Repository
| File Name            | Description |
|----------------------|-------------|
| `Titanic-Dataset.csv` | Titanic dataset used for EDA from kaggle|
| `task2.py`           | Python script that performs the entire EDA |
| `task2-01.png` to `task2-07.png` | Screenshots of key plots like histograms, boxplots, pairplots, and heatmaps |
| `README.md`          | Project summary and insights |

---

##  Key Steps Performed
1. Loaded and inspected the Titanic dataset.
2. Cleaned missing values and removed irrelevant columns.
3. Generated summary statistics (mean, std, median, etc.).
4. Plotted:
   - Histograms for distribution of features
   - Boxplots for survival vs age and fare
   - Correlation heatmap to detect relationships
   - Pairplot to visually explore feature interactions
5. Identified skewness, outliers, and multicollinearity.

---

##  Insights Discovered
- **Class Matters**: Passengers in higher classes had a greater chance of survival.
- **Age Factor**: Younger passengers were more likely to survive.
- **Gender Impact**: Though not visualized in this version, historically women had higher survival chances.
- **Fare Skewness**: Fare is right-skewed with several high outliers.
- **Multicollinearity**: Moderate correlation between Fare and Pclass was observed.

---

##  Screenshots
Below are visualizations saved as images:
- Histogram of features
- Boxplots (Survived vs Age, Fare vs Pclass)
- Heatmap of correlations
- Pairplot of selected features

Check the images: `task2-01.png` to `task2-07.png`

---
