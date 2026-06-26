import requests
 

dataset_id = "d_2bc812dbfd1e485638435fcdf7aac196"
'''
Resident Households By Household Size, Annual

Data from Jan 1980 to Dec 2025

Last updated: 09 Jun 2026, 23:00 SGT
SINGSTAT (Singapore Department of Statistics)

Source: SINGAPORE DEPARTMENT OF STATISTICS

Data Last Updated: 09/02/2026

Update Frequency: Annual

Footnotes: Data for 1980, 1990, 2000, 2010 and 2020 are based on the Census of Population while data for 1995, 2005, 2015 and 2025 are based on the General Household Survey. Data for all other years are based on the Comprehensive June Labour Force Survey. Survey estimates are subject to sampling variability.

Adapted from: https://tablebuilder.singstat.gov.sg/table/TS/M810371
'''
        
response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id="  + dataset_id)
with open('cached_households.json','w') as f:
    f.write(response.text)




'''
Household Sector Balance Sheet (End Of Period), Quarterly, Seasonally Adjusted

Data from Jan 1995 to Mar 2026

Last updated: 14 Jun 2026, 19:00 SGT
SINGSTAT (Singapore Department of Statistics)

Source: SINGAPORE DEPARTMENT OF STATISTICS

Data Last Updated: 26/05/2026

Update Frequency: Quarterly

Adapted from: https://tablebuilder.singstat.gov.sg/table/TS/M700982
'''

dataset_id = "d_c14a14d2f870e909268a9be5970e7d87"

response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id="  + dataset_id)
with open('cached_household_sector_balance.json','w') as f:
    f.write(response.text)



'''
Data from Jan 1961 to Apr 2026

Last updated: 27 May 2026, 22:01 SGT
SINGSTAT (Singapore Department of Statistics)

Source: SINGAPORE DEPARTMENT OF STATISTICS

Data Last Updated: 25/05/2026

Update Frequency: Monthly

Footnotes: The weighting pattern of the Consumer Price Index (CPI) was derived from the expenditure values collected from the Household Expenditure Survey (HES) 2023 and updated to 2024 values by taking into account price changes between 2023 and 2024.

Adapted from: https://tablebuilder.singstat.gov.sg/table/TS/M213751
'''
          
dataset_id = "d_bdaff844e3ef89d39fceb962ff8f0791"
response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id="  + dataset_id)
with open('cached_consumer_price_index.json','w') as f:
    f.write(response.text)
