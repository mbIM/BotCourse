import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import goslate



from weather import get_weather_data
from course import get_сourse
from wiki import get_summary
from сс import *

def main():

    TOKEN = "3d02e045e965c29c4c4a04606979e5c5b0aa3372fcd07a97d4fcfec0c799f52e46355eacac5affb5d9eb9"

    vk_session = vk_api.VkApi(token=TOKEN)


    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    hello = '''
       Привет, я повелитель Ада - Люци, и я всегда готова тебе помочь^.^
       Вот, что я умею:

       Я могу присылать различные мемы:
       -тм - мем из русского мультифандома
       -нм - научный мем 
       -дм - добрый мем

       Так же я могу скинуть цитатку:
       -ц - цитата
       
       И интересные слэнговые слова:
       -р - слэнговые слова

       Ещё я умею узнавать погоду в твоём городе, курс валют и выдавать краткие справки о том, что тебя интересует:
       -с <объект> - краткая справка о интересующем тебя объекте
       -п <город> - погода в твоём городе
       -к - курс валют
       '''

    gs = goslate.Goslate()

    ss = ['Ава — сокращённый вариант от слова "аватарка"; фотография пользователя в профиле соцсети. ',
          'Агриться — злиться, ругаться на кого-то.',
          'Бомбит — бесит, раздражает, напрягает. ',
          'Баттхёрт, бугурт — состояние человека'
          ', который негодует, испытывает гнев; нередко используется как синоним слова "бугурт";'
          ' произошло от английского слова butthurt (попная боль). ',
          'Бра, бро — уважительная и дружественная форма обращение от сокращённого английского слова brother (брат). ',
          'Бабецл — взрослая женщина, которую мальчики-подростки не считают сексуально привлекательной. ',
          'Варик — сокращённое от слова "вариант". ',
          'Го — пойдём, начинай, давай; от английского глагола go (давай, пойдём).',
          'Жиза — правда, жизненная ситуация, близкая читателю.',
          'Зашквар — позор, недостойно, плохо, не модно.',
          'ЛС — личные сообщения.',
          'По дэхе — чуть-чуть, немного.',
          'Абилка — способность, свойство человека или предмета. Например, "У нового "айфона" куча прикольных абилок".',
          'Ганк, ганкнуть — добиться своих целей подлыми методами.',
          'Грайнд (возм. гринд) — однообразная и нудная работа, необходимая для достижения какой-либо цели.']

    memes = {
        '-138383301' : ['456742203', '456741173', '456740947'],
        '-147286578' : ['456363035', '456362986', '456362982'],
        '-159146575' : ['456295687', '456311973', '456311966']
    }

    post = ['Если радуга долго держится, на нее перестают смотреть.',
            'В нашей семье считалось, что любую беду можно исправить чашкой чая.',
            'Лучшая маска, какую мы только можем надеть, — это наше собственное лицо.',
            'Можно ехать в одном вагоне, но в разные стороны.',
            'В шесть лет я хотел быть Колумбом, в семь – Наполеоном, а потом мои притязания постоянно росли.']

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg_text = event.text.lower()
            query = msg_text[3:]
            message_id = random.randint(0, 200000)


            if msg_text == "начать" or msg_text == "?":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=hello)

            elif msg_text[0:2] == "-с":
                vk.messages.send(user_id=event.user_id, random_id=message_id,  message=get_summary(query))

            elif msg_text[0:2] == "-п":
                try:
                    query = gs.translate(query, "en")
                    response = get_weather_data(query)
                except Exception:
                    response = ":( Сервис не доступен"

                vk.messages.send(user_id=event.user_id, random_id=message_id, message=response)

            elif msg_text[0:2] == "-к":
                response = "{0} рублей за 1 доллар \n {1} рублей за 1 евро \n {2} рублей за 10 юаней \n {3} рублей за фунт"
                response = response.format(get_сourse("R01235"), get_сourse("R01239"), get_сourse("R01375"), get_сourse("R01035"))
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=response)


            elif msg_text[0:2] == '-ц':
                vk.messages.send(user_id=event.user_id, random_id=message_id,
                                 message=random.choice(post))

            elif msg_text[0:3] == "-тм":
                vk.messages.send(user_id=event.user_id, random_id=message_id,
                                 message=":)",
                                 attachment='photo{0}_{1}'.format('-138383301', random.choice(memes['-138383301'])))

            elif msg_text[0:3] == "-дм":
                vk.messages.send(user_id=event.user_id, random_id=message_id,
                                 message=":)",
                                 attachment='photo{0}_{1}'.format('-147286578', random.choice(memes['-147286578'])))

            elif msg_text[0:3] == "-нм":
                vk.messages.send(user_id=event.user_id, random_id=message_id,
                             message=":)",
                             attachment='photo{0}_{1}'.format('-159146575', random.choice(memes['-159146575'])))

            elif msg_text[0:3] == "-р":
                vk.messages.send(user_id=event.user_id, random_id=message_id,
                                 message=random.choice(ss))
            else:
                vk.messages.send(user_id=event.user_id, random_id=message_id, message="Я вас не понимаю ;(")





print('ok')



if __name__ == '__main__':
    main()
