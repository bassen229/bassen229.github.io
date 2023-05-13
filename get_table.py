import requests
import numpy as np
import pandas as pd

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json  = r.json()
df = pd.DataFrame(json['teams'])
id_dict = {}
for it in df[['name','id']].values:
    id_dict[it[1]] = it[0]

url = 'https://fantasy.premierleague.com/api/fixtures/'
r = requests.get(url)
json = r.json()
df = pd.DataFrame(json)

df['team_a'] = df['team_a'].map(id_dict)
df['team_h'] = df['team_h'].map(id_dict)
df['kickoff_time'] = pd.to_datetime(df['kickoff_time']).dt.strftime("%Y-%m-%d %H:%M:%S")

df = df[['kickoff_time','team_a','team_a_score','team_h','team_h_score']].T
# Convert the DataFrame to a JSON object
json_obj = df.to_json(orient='records')

# Save the JSON object to a file
with open('C:\\Users\\sebas\\OneDrive\\premierleaguepage\\bassen229.github.io\\fixtures.json', 'w') as f:
    f.write(json_obj)
