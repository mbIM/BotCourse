import wikipedia

def get_summary(name):
    try:
        wikipedia.set_lang("ru")
        russia = wikipedia.page(name)
        return "{0}\nБольше подробностей по ссылке - {1}".format(russia.summary, russia.url)
    except Exception:
        return " :( Страничка не найдена"

if __name__ == "__main__":
    print(get_summary("Химки"))