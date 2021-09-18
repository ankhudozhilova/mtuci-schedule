from senders.senderController import SenderController


class BaseCommand:
    answer = {}
    sender_controller = SenderController()
    command = {}

    def setCommand(self, command: dict) -> None:
        self.command = command

    def makeAnswer(self, msg: str) -> None:
        self.answer = {
            "text": msg,
            "chat_id": self.command["chat_id"],
            "service": self.command["service"],
        }

    def sendAnswer(self):
        self.sender_controller.sendMessage(self.answer)
