# Script to scrape data from Puerto Rico's Department of Education
import pandas as pd
import requests
import json


# I need to obtain schools' codes. I need to load df containing school codes
escuelasData= pd.read_csv('escuelasData.csv')

school_codes = escuelasData['codigo']


# Tyler's work.
url_appendix = '&sv=2019-02-02&ss=t&srt=o&sp=r&se=2024-02-13T23:32:55Z&st=2020-02-13T15:32:55Z&spr=https&sig=2Ru59MA2m937gKY3qb1qVCeg2SnBiS84KQEGWgo2dqw='

function_list = ['EnrollmentByGradeNEW()', 'EnrollmentByAcademicYearNEW()']

# Creating empty dictionary
enrollment_by_acYear_dict = []


for code in school_codes:
    
    response = requests.get(f'https://schoolreportcardstorage.table.core.windows.net/EnrollmentByAcademicYearNEW()?$filter=PartitionKey%20eq%20%27{code}%27{url_appendix}',
                                headers={
                                    'Accept': 'application/json;odata=nometadata',
                                    'Content-Type': 'text/plain; charset=utf-8',
                                    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
                                })
    j = response.json()
    x = pd.json_normalize(j['value'])
    #x = x.reset_index()
    enrollment_by_acYear_dict.append(x)



enrollment_by_acYear = pd.concat(enrollment_by_acYear_dict)
enrollment_by_acYear.to_csv('enrollment_by_acYear.csv', index=False)

df = pd.read_csv('enrollment_by_acYear.csv')

