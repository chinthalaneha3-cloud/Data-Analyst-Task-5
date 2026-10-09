import pandas as pd
import matplotlib.pyplot as plt

# 1. Data Load
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Basic Info
print(df.head())
print(df.describe())
print(df['Survived'].value_counts())

# 3. Age missing fill
df['Age'].fillna(df['Age'].median(), inplace=True)

# 4. Graph 1 - Age
plt.hist(df['Age'], bins=20)
plt.title("Age")
plt.show()

# 5. Graph 2 - Survival
df['Survived'].value_counts().plot(kind='bar')
plt.title("Survived 0=Died 1=Alive")
plt.show()

# 6. Graph 3 - Pclass vs Survived
pd.crosstab(df['Pclass'], df['Survived']).plot(kind='bar')
plt.title("Pclass vs Survival")
plt.show()

# 7. Graph 4 - Age vs Fare
plt.scatter(df['Age'], df['Fare'])
plt.title("Age vs Fare")
plt.show()

