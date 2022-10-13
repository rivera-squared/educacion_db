# Script to scrape data from Puerto Rico's Department of Education
import pandas as pd
import requests
import json


escuelasData= pd.read_csv('escuelasData.csv')

school_codes = escuelasData['codigo']
# Creating empty dictionary
aprovechamiento_raw = []
code = '35295'

for code in school_codes:
        
    response = requests.get(f'https://conocetuescuelapr.dde.pr/metricasData/{code}',
                                headers={
                                    'Accept': 'application/json',
                                    #'Content-Type': 'text/plain; charset=utf-8',
                                    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
                                })
    j = response.json()
    aprovechamiento_raw.append(j)
    

aprovechamiento = []
nums = list(range(0,len(aprovechamiento_raw),1))

for num in nums:
    x = pd.json_normalize(aprovechamiento_raw[num])
    aprovechamiento.append(x)

aprovechamiento = pd.concat(aprovechamiento)    
aprovechamiento.to_csv('aprovechamiento.csv', index = False)
