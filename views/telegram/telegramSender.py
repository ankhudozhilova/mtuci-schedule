import requests

import views.baseSender as bs


class TelegramSender(bs.BaseSender):
    service = "telegram"

    def __init__(self):
        super().__init__()
        self.url = f"https://api.telegram.org/bot{self.token}/"

    def sendMessage(self, msg: str, id: str) -> None:
        requests.get(self.url + f"sendMessage?chat_id={id}&text={msg}").json()

    def getCommands(self) -> list:
        answers = []
        queries = requests.get(self.url + f"getUpdates").json()

        if queries["ok"]:
            answers = [{"text": query["message"]["text"],
                        "chat_id": query["message"]["chat"]["id"],
                        "time": query["message"]["date"],
                        "service": "telegram"} for query in queries["result"]]

        return answers

    def getCommand(self) -> dict:
        return self.getCommands()[-1]
