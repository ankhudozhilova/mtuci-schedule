import pandas as pd


class BaseSender:
    url = ""
    token = ""
    service = ""

    def __init__(self):
        self.token = pd.read_csv("data/tokens.csv").get(self.service)[0]

    def get_message(self) -> dict:
        return dict()

    def send_message(self, msg: str, id: str) -> None:
        pass