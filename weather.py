import requests
from bs4 import BeautifulSoup


def get_html(city):
    """
    Принимает аргументом строку название города на латинице, создаёт из этого url
    Пример:
    https://yandex.ru/pogoda/moscow

    и возвращает нам html-код странички по указанному адресу
    """
    url = "https://yandex.ru/pogoda/"
    response = requests.get(url + city)
    return BeautifulSoup(response.content, "lxml")


def get_temp(html):
    """
    Принимает аргументом html-код, ищёт в нём тег span c классом temp__value и возвращает содержимое
    этого тега (температура воздуха)
    """
    return html.find("span", {'class': 'temp__value'}).text


def get_condition(html):
    """
    Принимает аргументом html-код, ищёт в нём тег div c классом fact__condition и возвращает содержимое
    этого тега (Пасмурно/облачно/дождь)
    """
    return html.find("div", {'class': 'fact__condition'}).text


def get_wind_speed(html):
    """
    Принимает аргументом html-код, ищёт в нём тег span c классом wind-speed и возвращает содержимое
    этого тега (Скорость ветра)
    """
    return html.find("span", {'class': 'wind-speed'}).text


def get_term_value(html):
    """
    Принимает аргументом html-код, ищёт в нём тег dl c классом fact__pressure возвращает содержимое
    этого тега (Давление)
    """
    return html.find("dl", {'class': 'fact__pressure'}).dd.text


def get_humidity(html):
    """
    Принимает аргументом html-код, ищёт в нём тег dl c классом fact__humidity возвращает содержимое
    этого тега (Влажность)
    """
    return html.find("dl", {'class': 'fact__humidity'}).dd.text


def get_time_of_day(html):
    """
    Принимает аргументом html-код, ищёт в нём время рассвета и время заката и текущее время
    Потом переводит всё это в минуты и путём сравнение узнаёт ночь сейчас или день. По итогу работы возвращает
    смайлик луны или солнца
    """
    time_now = html.find("time", {'class': 'time'}).text
    time_now = time_now[-5:]
    time_now = int(time_now[0:2]) * 60 + int(time_now[3:])

    sunrice = html.find("dl", {'class': 'sunrise-sunset__description_value_sunrise'}).dd.text
    sunrice = int(sunrice[0:2]) * 60 + int(sunrice[3:])

    sunset = html.find("dl", {'class': 'sunrise-sunset__description_value_sunset'}).dd.text
    sunset = int(sunset[0:2]) * 60 + int(sunset[3:])

    if time_now >= sunset or time_now < sunrice:
        return "\U0001F31A"
    elif time_now >= sunrice and time_now < sunset:
        return "\U0001F31E"


def get_weather_data(city):
    """
    Принимает аргументом название города латинскими буквами, чтобы передать его в функцию get_html.
    По итогу работы возвращает строку со всеми данными о погоде в интересующем городе. В случае если возникает
    какая-то ошибка, возвращает строку, о том, что такого города нет
    """
    try:
        html = get_html(city)

        temp_value = get_temp(html)
        weather_condition = get_condition(html)
        time_day = get_time_of_day(html)
        wind = "Ветер " + get_wind_speed(html) + " м/с"
        term = "Давление " + get_term_value(html)
        term_value = "Влажность " + get_humidity(html)

        return " {0} {1} {2} {3} {4} {5}".format(temp_value, weather_condition, time_day, wind, term, term_value)


    except Exception:
        return " :( Город не найден"


if __name__ == "__main__":
    """
    Проблема парсинга в том, что у яндекс.погоды не все ссылки в человекопонятном формате, допустим
    если Москва и Лондон ну и большинство российских городов вполне можно найти по url в котором есть их
    название на транслите, то допустим Киев представлен как 143.
    https://yandex.ru/pogoda/143
    """
    print(get_weather_data("london"))
    print(get_weather_data("moscow"))
    print(get_weather_data("kiev"))
    print(get_weather_data("143"))
