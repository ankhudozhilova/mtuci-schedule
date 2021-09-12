from senders.senderController import SenderController
from commands.commandController import CommandController


class Application:
    senderController = SenderController()
    commandController = CommandController()

    def start(self):
        cmds = self.senderController.getCommands()
        for cmd in cmds:
            self.commandController.executeCommand(cmd)