import requests
import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Real API endpoint
url = "https://api.sleeper.app/v1/players/nfl"

# Debug: show that the script is running
print("Requesting data from Sleeper API...")
response = requests.get(url)
print("Response status code:", response.status_code)

# If the API call is successful
if response.status_code == 200:
    data = response.json()

    # Convert JSON dictionary to list of player data
    players = list(data.values())
    df = pd.DataFrame(players)

    # Optional: only show selected columns if they exist
    columns_to_show = ['full_name', 'team', 'position', 'age']
    available_columns = [col for col in columns_to_show if col in df.columns]

    # Print top 10 players with selected info
    print(df[available_columns].head(10))
else:
    print("Failed to fetch data:", response.status_code)