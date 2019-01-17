import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def get_сourse (id):
	return str(xml.find("valute",  {'id': id}).value.text)


if __name__ == '__main__':
	print(get_сourse("R01235"), "рублей за 1 доллар")
	print(get_сourse("R01239"), "рублей за 1 евро")
	print(get_сourse("R01375"), "рублей за 10 юаней")