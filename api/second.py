import requests
import pandas as pd
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET


url = "http://www.cbr.ru/scripts/XML_daily.asp"
 
currencies = ['BYR', 'USD', 'EUR', 'KZT', 'UAH', 'AZN', 'KGS', 'UZS', 'GEL']
date_from = datetime(2003, 1, 1)
date_to = datetime(2004, 6, 1)
df = pd.DataFrame(columns=["date", 'BYR', 'USD', 'EUR', 'KZT', 'UAH', 'AZN', 'KGS', 'UZS', 'GEL'])
date = start_date
while date <= end_date:
    response = requests.get(f"{url}?date_req={date.strftime('%d/%m/%Y')}")
    response.raise_for_status()
    data = response.content
    root = ET.fromstring(response.content)
    rates = {elem.find('CharCode').text: round(float(elem.find('Value').text.replace(',','.'))/int(elem.find('Nominal').text),8) for elem in root.findall('Valute') if elem.find('CharCode').text in currencies}
    df.loc[date.strftime('%Y-%m')] = [date.strftime('%Y-%m')] + [rates.get(currency, '') for currency in currencies]
 
    if date.month == 12:
        date = date.replace(year=date.year + 1, month=1)
    else:
        date = date.replace(month=date.month + 1)
with open('student_works/currency.csv', 'w',newline='') as file:
	df.to_csv(file,index=False)