from bs4 import BeautifulSoup
import pandas as pd
import requests

# # Wikipedia URL for list of presidents
# url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

# response = requests.get(url)
# # print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup)

# # # Find the table containing presidents' data
# table = soup.find("table", {"class": "wikitable"})

# # Lists to hold president names and terms
# names = []
# terms = []

# # # Extracting president names and terms from the table rows
# for row in table.find_all("tr")[1:]:  # Skipping the header row
#     cells = row.find_all("td")
#     if cells:
#         names.append(cells[1].get_text(strip=True))  # Name is in the second cell
#         terms.append(cells[2].get_text(strip=True))  # Term is in the third cell

# # # Creating a DataFrame to store the data
# df_presidents = pd.DataFrame({
#     "Name": names,
#     "Term": terms
# })

# # # Display the DataFrame
# print(df_presidents)

# Optionally, save to CSV
# df_presidents.to_csv("us_presidents.csv", index=False)

# URL containing S&P 500 company data
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Finding the table containing S&P 500 companies
table = soup.find("table", {"id": "constituents"})

# Lists to hold S&P 500 company data
tickers = []
names = []
sectors = []

# Extracting ticker, company name, and sector from the table rows
for row in table.find_all("tr")[1:]:  # Skipping the header row
    cells = row.find_all("td")
    if cells:
        tickers.append(cells[0].get_text(strip=True))  # Ticker symbol
        names.append(cells[1].get_text(strip=True))    # Company name
        sectors.append(cells[3].get_text(strip=True))  # Sector

# Creating a DataFrame to store the data
df_sp500 = pd.DataFrame({
    "Ticker": tickers,
    "Company": names,
    "Sector": sectors
})
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns',None)
# Display the DataFrame
print(df_sp500)

# Optionally, save to CSV
df_sp500.to_csv("sp500_companies.csv", index=False)
