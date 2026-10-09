# Task 5: Exploratory Data Analysis (EDA) - Titanic Dataset

### 1. Objective
To perform Exploratory Data Analysis (EDA) on the Titanic dataset to extract insights, identify trends, patterns, and anomalies in passenger survival.

### 2. Dataset
- **Source:** Titanic Dataset from Kaggle
- **Link:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- **Size:** 891 rows x 12 columns
- **Target Column:** Survived (0 = Died, 1 = Survived)

### 3. Tools & Libraries
- Python
- Pandas - for data loading and analysis
- Matplotlib - for data visualization

### 4. Code Workflow (Step-by-Step)

**Step 1: Data Loading**
Loaded data directly from GitHub URL using `pd.read_csv()`

**Step 2: Basic Information**
- `df.head()` - Displays first 5 rows
- `df.describe()` - Statistical summary (Mean Age = 29.6, Mean Fare = 32)
- `df['Survived'].value_counts()` - Shows 549 Died and 342 Survived

**Step 3: Data Cleaning**
- Handled missing values