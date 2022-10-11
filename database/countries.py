import pandas as pd
pd.read_html('https://www.iban.com/country-codes')[0][['Alpha-3 code', 'Country']].rename(columns={'Alpha-3 code': 'country_code', 'Country': 'country_name'}).to_csv('../Resources/countries.csv', index=False)