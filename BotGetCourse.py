import vk_api
import random

from грп import *

token = "3d02e045e965c29c4c4a04606979e5c5b0aa3372fcd07a97d4fcfec0c799f52e46355eacac5affb5d9eb9"

vk = vk_api.VkApi(token=token)

vk._auth_token()

flags = {
    "-д" : "R01235",
    "-ю" : "R01375",
    "-ф" : "R01035"
}

names = {
    '-д' : ' рублей за 1 доллар',
    '-ю' : ' рублей за 1 юань',
    '-ф' : ' рублей за один фунт'
}

while True:
    messages = vk.method("messages.getConversations", {"count": 21, "filter": "unanswered"})
    if messages["count"] > 0:
        id = messages["items"][0]['last_message']['from_id']
        #vk.method("messages.send",{"user_id": id, "random_id": random.randint(1, 200000), "message": "Привет!"})
        msg = messages["items"][0]["last_message"]["text"].lower()
        flag = flags.get(msg[5: ])
        name = names.get(msg[5: ])

        if len(msg) == 7 and msg[0:4] == "курс" and flag != None and name != None:
         vk.method("messages.send",{"user_id": id, "random_id": random.randint(1, 200000), "message": getCourse(flag) + name})