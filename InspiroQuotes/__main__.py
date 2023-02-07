from requests import get


class Quote:
    def __init__(self):
        self.url = "https://inspiro-bot.some-1hing.repl.co/quotes"

    def quote(self):
        try:
            quote = get(self.url).json()["quotes"]
            return quote
        except Exception as e:
            return e

    def img_quote(self):
        return self.quote()

    def text_quote(self):
        try:
            quote = get(self.url).json()["textQuotes"]
            return quote
        except Exception as e:
            return e
