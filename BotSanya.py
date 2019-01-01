import vk_api
import random
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

        if msg == "Привет":
            vk.method("messages.send", {"user_id": id, "random_id": random.randint(1, 200000), "message": "Добро пожаловать"})
        elif msg == "Воины":
            vk.method("messages.send", {"user_id": id, "random_id": random.randint(1, 200000),
                                        "message": "Выбери бойца:", "photo" : {"id": 456246674,
                                                                               "album_id": -64,"owner_id": 483718643}})