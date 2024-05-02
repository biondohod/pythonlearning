import requests
import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET

def fetch_exchange_rates(date, currency_codes):
    url = f"http://127.0.0.1:8000/scripts/XML_daily.asp?date_req={date.strftime('%d/%m/%Y')}"
    response = requests.get(url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    exchange_rates = {}
    for elem in root.findall("Valute"):
        currency_code = elem.find("CharCode").text
        if currency_code in currency_codes:
            value = float(elem.find("Value").text.replace(",", "."))
            nominal = int(elem.find("Nominal").text)
            exchange_rate = round(value / nominal, 8)
            exchange_rates[currency_code] = exchange_rate
    return exchange_rates


def increment_month(date):
    if date.month == 12:
        return date.replace(year=date.year + 1, month=1)
    else:
        return date.replace(month=date.month + 1)


def main():
    currency_codes = ["BYR", "USD", "EUR", "KZT", "UAH", "AZN", "KGS", "UZS", "GEL"]
    date_from = datetime(2003, 1, 1)
    date_to = datetime(2023, 6, 1)
    data_frame = pd.DataFrame(columns=["date"] + currency_codes)
    current_date = date_from
    while current_date <= date_to:
        exchange_rates = fetch_exchange_rates(current_date, currency_codes)
        data_frame.loc[current_date.strftime("%Y-%m")] = [
            current_date.strftime("%Y-%m")
        ] + [exchange_rates.get(currency, "") for currency in currency_codes]
        current_date = increment_month(current_date)
    with open("student_works/currency.csv", "w", newline="") as file:
        data_frame.to_csv(file, index=False)


if __name__ == "__main__":
    main()
