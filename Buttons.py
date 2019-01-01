import json
import random
import sys
import lxml
import vk_api

token = "3d02e045e965c29c4c4a04606979e5c5b0aa3372fcd07a97d4fcfec0c799f52e46355eacac5affb5d9eb9"

vk = vk_api.VkApi(token=token)

vk._auth_token()


def create_button(type, color, payload, label):
    return {
        "action": {
            "type": type,
            "payload": payload,
            "label": label
        },
        "color": color
    }


keyboard = {
    "one_time": True,
    "buttons": [
        [create_button("text", "default", "{\"button\": \"1\"}", "0")],
        [create_button("text", "default", "{\"button\": \"2\"}", "1")],
        [create_button("text", "default", "{\"button\": \"3\"}", "2")],
        [create_button("text", "default", "{\"button\": \"4\"}", "3")],
        [create_button("text", "default", "{\"button\": \"5\"}", "4")],
        [create_button("text", "default", "{\"button\": \"6\"}", "5")],
        [create_button("text", "default", "{\"button\": \"7\"}", "6")],
        [create_button("text", "default", "{\"button\": \"8\"}", "7")],
        [create_button("text", "default", "{\"button\": \"9\"}", "8")],
        [create_button("text", "default", "{\"button\": \"10\"}", "9")]
    ]
}

keyboard1 = {
    "one_time": True,
    "buttons": [
        [create_button("text", "default", "{\"button\": \"1\"}", "+")],
        [create_button("text", "default", "{\"button\": \"2\"}", "-")],
        [create_button("text", "default", "{\"button\": \"3\"}", "/")],
        [create_button("text", "default", "{\"button\": \"4\"}", "*")],
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
keyboard = str(keyboard.decode("utf-8"))

keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode("utf-8")
keyboard1 = str(keyboard1.decode("utf-8"))

while True:
    messages = vk.method("messages.getConversations", {"count": 21, "filter": "unanswered"})

    if messages["count"] >= 1:
        text = messages["items"][0]["last_message"]["text"]
        id = messages["items"][0]['last_message']['from_id']
        message_text = messages["items"][0]["last_message"]["text"].lower()
        list = ["+", "-", "/", "*"]

    if message_text == "начать":
        vk.method(
            "messages.send", {
                "user_id": id,
                "random_id": random.randint(1, 200000),
                "message": "Хелло",
                "keyboard": keyboard
            })

    elif int(message_text) in range(0, 10):
        vk.method(
            "messages.send", {
                "user_id": id,
                "random_id": random.randint(1, 200000),
                "message": "выберите операцию",
                "keyboard": keyboard1
            })

    elif str(message_text) in list:
        vk.method(
            "messages.send", {
                "user_id": id,
                "random_id": random.randint(1, 200000),
                "message": "выберите второе число",
                "keyboard": keyboard
            })
    else:
        print("katya durak")
    # break
