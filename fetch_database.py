import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define headers and URL
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
url = 'https://beyondparallel.csis.org/database-north-korean-provocations/'

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table in the HTML
table = soup.find('table', class_='responsive display nowrap data-t data-t wpDataTable wpDataTableID-55')

# Initialize an empty list to store the data
data = []

# Iterate over table rows, skipping the header row
for row in table.find('tbody').find_all('tr'):
    cells = row.find_all('td')
    
    if len(cells) == 5:
        data.append([cell.get_text(strip=True) for cell in cells])

# Create a DataFrame
src_df = pd.DataFrame(data, columns=['date', 'type', 'event', 'description', 'resources'])

df = src_df.copy()

# Process date strings
df['year'] = pd.to_datetime(df['date']).dt.strftime('%Y')
df['week_number'] = pd.to_datetime(df['date']).dt.strftime('%-U')
df['month_year'] = pd.to_datetime(df['date']).dt.strftime('%m-%Y')
df['weekday'] = pd.to_datetime(df['date']).dt.strftime('%A')

# Other insights from the description field? 
# Ask LLM to parse and summarize any mentions of launch locations, missile range/trajectory and landing areas, i.e., East Sea/Sea of Japan.

# Mentions of Kim Jong Un
df['mentions_kim'] = df['description'].str.contains("Kim Jong Un|Kim Jong-un")

# Export raw original file
src_df.to_json('data/raw/north_korea_provocations_1958_present.json', indent=4, orient='records')
src_df.to_csv('data/raw/north_korea_provocations_1958_present.csv', index=False)

# Export processed file
df.to_json('data/processed/north_korea_provocations_1958_present.json', indent=4, orient='records')
df.to_csv('data/processed/north_korea_provocations_1958_present.csv', index=False)