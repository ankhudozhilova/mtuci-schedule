import pandas as pd


class BaseSender:
    url = ""
    token = ""
    service = ""

    def __init__(self):
        self.token = pd.read_csv("data/tokens.csv").get(self.service)[0]

    def getCommand(self) -> dict:
        return dict()

    def sendMessage(self, msg: str, id: str) -> None:
        pass