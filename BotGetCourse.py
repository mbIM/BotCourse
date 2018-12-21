import vk_api
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import lxml

token = "3d02e045e965c29c4c4a04606979e5c5b0aa3372fcd07a97d4fcfec0c799f52e46355eacac5affb5d9eb9"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"count": 21, "filter": "unanswered"})
    if messages["count"] > 0:
        id = messages["items"][0]['last_message']['from_id']
        #vk.method("messages.send",{"user_id": id, "random_id": random.randint(1, 200000), "message": "Привет!"})
        msg = messages["items"][0]["last_message"]["text"]
        if msg == "курс":

            url = "http://www.cbr.ru/scripts/XML_daily.asp?"

            today = datetime.today()
            today = today.strftime("%d/%m/%Y")

            payload = {"date_req" : today}

            responce = requests.get(url, params=payload)

            xml = BeautifulSoup(responce.content, "lxml")

            def getCourse (id):
                return xml.find("valute", {'id': id}).value.text

            vk.method("messages.send",{"user_id": id, "random_id": random.randint(1, 200000), "message": (getCourse("R01235") + " рублей за 1 доллар")})