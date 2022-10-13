# Script to scrape data from Puerto Rico's Department of Education
import pandas as pd
import requests
import json


    response = requests.get('https://conocetuescuelapr.dde.pr/escuelasData',
                                headers={
                                    'Accept': 'application/json',
                                    #'Content-Type': 'text/plain; charset=utf-8',
                                    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
                                })
    j = response.json()

nums = list(range(0, len(j),1))

escuelasData = []

for num in nums:
    x = pd.json_normalize(j[num])
    escuelasData.append(x)

escuelasData = pd.concat(escuelasData)
escuelasData.to_csv('escuelasData.csv', index =False)
