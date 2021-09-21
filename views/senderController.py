from views.telegram.telegramSender import TelegramSender


class SenderController:
    senders = {"telegram": TelegramSender()}

    def getCommands(self) -> list:
        tmp, cmds = [sender.getCommands() for sender in self.senders.values()], []
        _ = [cmds.extend(cmd) for cmd in tmp]
        return cmds

    def sendMessage(self, answer: dict) -> None:
        self.senders[answer["service"]].sendMessage(answer["text"], answer["chat_id"])
