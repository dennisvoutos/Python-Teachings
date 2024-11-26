# # data_visualization_basics.py
# import numpy as np
# import pandas as pd
# # from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Recap on NumPy
# # NumPy for scientific computing, data science, and machine learning
# array1 = np.array([1, 2, 3, 4, 5])
# array2 = np.array([10, 20, 30, 40, 50])

# # Plotting with Matplotlib
# plt.figure(figsize=(10, 6))
# plt.plot(array1, array2, marker='o')
# plt.title("Line Plot Example")
# plt.xlabel("Array 1")
# plt.ylabel("Array 2")
# plt.show()

# # Recap on Pandas
# data = {
#     "Name": ["Anna", "Ben", "Charlie", "David"],
#     "Age": [23, 45, 34, 32],
#     "Score": [87, 92, 68, 74]
# }
# df = pd.DataFrame(data)

# # Pandas and Matplotlib for plotting
# plt.figure(figsize=(10, 6))
# plt.bar(df["Name"], df["Score"], color="skyblue")
# plt.title("Bar Plot Example")
# plt.xlabel("Name")
# plt.ylabel("Score")
# plt.show()

# # Seaborn example using the tips dataset
# tips = sns.load_dataset("tips")

# # Seaborn histogram
# plt.figure(figsize=(10, 6))
# sns.histplot(tips["total_bill"], kde=True, color="blue")
# plt.title("Histogram of Total Bill")
# plt.xlabel("Total Bill")
# plt.show()

# # Seaborn scatter plot with regression line
# plt.figure(figsize=(10, 6))
# sns.regplot(x="total_bill", y="tip", data=tips, color="green")
# plt.title("Total Bill vs Tip")
# plt.xlabel("Total Bill")
# plt.ylabel("Tip")
# plt.show()

# ------------------------------------------------------------------------------------------------------

# movies_series_visualizations.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the movies and series dataset
df = pd.read_csv("data.csv")

# # Distribution of Average Ratings
# plt.figure(figsize=(10, 6))
# sns.histplot(df["averageRating"], bins=20, color="coral")
# plt.title("Distribution of Average Ratings")
# plt.xlabel("Average Rating")
# plt.ylabel("Frequency")
# plt.show()

# # Most Popular Genres (count of occurrences)
# plt.figure(figsize=(14, 8))
# genres = df["genres"].str.get_dummies(sep=',').sum().sort_values(ascending=False)
# genres.plot(kind='bar', color="skyblue")
# plt.title("Most Popular Genres")
# plt.xlabel("Genres")
# plt.ylabel("Frequency")
# plt.show()

# # Number of Movies/Series over the Years
# plt.figure(figsize=(12, 6))
# sns.histplot(df["releaseYear"], bins=30, color="purple")
# plt.title("Number of Movies/Series Released Over the Years")
# plt.xlabel("Release Year")
# plt.ylabel("Count")
# plt.show()

# # Relationship between Ratings and Number of Votes
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x="averageRating", y="numVotes", data=df, color="teal", alpha=0.5)
# plt.title("Relationship Between Ratings and Number of Votes")
# plt.xlabel("Average Rating")
# plt.ylabel("Number of Votes")
# plt.yscale("log")  # Use log scale for better visualization
# plt.show()

# Heatmap of Rating vs Year, highlighting the density of ratings over time
ratings_by_year = df.pivot_table(values='averageRating', index='releaseYear', columns='genres', aggfunc='mean')
plt.figure(figsize=(14, 8))
sns.heatmap(ratings_by_year, cmap="YlGnBu", linecolor="white", linewidth=0.5)
plt.title("Heatmap of Average Ratings by Year and Genre")
plt.xlabel("Genres")
plt.ylabel("Release Year")
plt.show()
