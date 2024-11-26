# 1. Basic Types Using Constructors
print("=== Basic Types Using Constructors ===")
int_var = int(5)
float_var = float(5.5)
str_var = str("Hello")
bool_var = bool(True)
print("Integer:", int_var, "| Float:", float_var, "| String:", str_var, "| Boolean:", bool_var)


# 2. Python Objects and Classes (OOP)
print("\n=== Object-Oriented Programming in Python ===")

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}."

# Creating an object
student1 = Student("Alice", 20, "Data Science")
print(student1.introduce()) 

# Inheritance Example
class GraduateStudent(Student):
    def __init__(self, name, age, course, thesis):
        super().__init__(name, age, course)
        self.thesis = thesis

    def introduce(self):
        return f"{super().introduce()} My thesis is on {self.thesis}."

grad_student = GraduateStudent("Bob", 25, "Computer Science", "Machine Learning")
print(grad_student.introduce())


# 3. Working with NumPy
import numpy as np

print("\n=== NumPy Array Operations ===")
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Array + 10:", arr + 10)
print("Mean:", np.mean(arr), "| Sum:", np.sum(arr), "| Standard Deviation:", np.std(arr))

# Reshaping and Broadcasting
matrix = np.arange(1, 10).reshape(3, 3)
print("\nReshaped 3x3 Matrix:\n", matrix)
print("Matrix * 2 (Broadcasted):\n", matrix * 2)


# 4. Data Manipulation and Analysis using Pandas
import pandas as pd

print("\n=== Data Manipulation with Pandas ===")
# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Cathy", "Dave"],
    "Age": [24, 27, 22, 32],
    "Score": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Data Analysis
print("\nDescriptive Statistics:\n", df.describe())

# Filtering Data
filtered_df = df[df['Score'] > 80]
print("\nFiltered DataFrame (Score > 80):\n", filtered_df)


# 5. Data Visualization with Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Visualization
print("\n=== Data Visualization ===")
plt.figure(figsize=(8, 4))
sns.histplot(df['Score'], bins=5, color="skyblue")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 4))
sns.scatterplot(x="Age", y="Score", data=df, color="purple")
plt.title("Score vs Age")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()


# 6. Web Scraping with BeautifulSoup and Pandas
from bs4 import BeautifulSoup
import requests

# A. Scraping a List of US Presidents from Wikipedia
print("\n=== Web Scraping: List of US Presidents ===")
url_presidents = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url_presidents)
soup = BeautifulSoup(response.text, "html.parser")
table_presidents = soup.find("table", {"class": "wikitable"})

# Reading into a Pandas DataFrame
df_presidents = pd.read_html(str(table_presidents))[0]
print("US Presidents (Top 5):\n", df_presidents.head())

# B. Scraping S&P 500 Companies
print("\n=== Web Scraping: S&P 500 Companies ===")
url_sp500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response_sp500 = requests.get(url_sp500)
soup_sp500 = BeautifulSoup(response_sp500.text, "html.parser")
table_sp500 = soup_sp500.find("table", {"id": "constituents"})

# Reading into a Pandas DataFrame
df_sp500 = pd.read_html(str(table_sp500))[0]
print("S&P 500 Companies (Top 5):\n", df_sp500.head())
