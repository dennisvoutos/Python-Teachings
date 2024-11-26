# Import necessary libraries
import pandas as pd

# 1. Read and write data using Pandas

# Reading data from a CSV file
# Make sure that you download the dataset from Moodle, and have it in the same directory as the code!
url = 'data.csv'
data = pd.read_csv(url)
# # Display the first few rows of the dataset
print(data.head())
print(data.columns)

# Check for missing values in the dataset
print("Missing values per column:\n", data.isna().sum())

# Fill missing values in 'averageRating' and 'numVotes' with their respective column means
data['averageRating'].fillna(data['averageRating'].mean(), inplace=True)
data['numVotes'].fillna(data['numVotes'].mean(), inplace=True)

# Drop rows with missing values in 'title' or 'releaseYear' (assuming these are critical fields)
cleaned_data = data.dropna(subset=['title', 'releaseYear'])

# Verify that missing values have been handled
print("Missing values after cleaning:\n", cleaned_data.isna().sum())

# 3. Data Manipulation

# Creating a Pandas Series for unique genres and their frequency
genre_counts = cleaned_data['genres'].value_counts()
print("Genre Frequency:\n", genre_counts)

# Extract a subset of the data for high-rated movies or series
high_rated_data = cleaned_data[cleaned_data['averageRating'] > 8.5]
print("High-rated movies/series:\n", high_rated_data.head())

# Filtering for movies or series with a high number of votes (e.g., over 1 million votes)
popular_data = cleaned_data[cleaned_data['numVotes'] > 1_000_000]
print("Popular movies/series (over 1M votes):\n", popular_data.head())

# 4. Data Analysis and Aggregation

# Descriptive statistics for numerical columns
print("Descriptive statistics:\n", cleaned_data[['averageRating', 'numVotes', 'releaseYear']].describe())

# Grouping by 'releaseYear' to analyze the average rating and total votes per year
yearly_stats = cleaned_data.groupby('releaseYear').agg({
    'averageRating': 'mean',
    'numVotes': 'sum'
}).sort_index(ascending=False)
print("Yearly stats (Average Rating & Total Votes):\n", yearly_stats)

# Analyzing top genres by average rating
genre_ratings = cleaned_data.groupby('genres')['averageRating'].mean().sort_values(ascending=False)
print("Top genres by average rating:\n", genre_ratings.head())

# Saving cleaned and processed data back to a CSV
cleaned_data.to_csv('cleaned_movies_series_output.csv', index=False)