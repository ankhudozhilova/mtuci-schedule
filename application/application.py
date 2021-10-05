from views.senderController import SenderController
from controllers.commands.commandController import CommandController
from models.parsers.baseParser import BaseParser

import pickle


class Application:
    senderController = SenderController()
    commandController = CommandController()
    baseParser = BaseParser()

    def __init__(self):
        self.old_cmds = []
        with open("data/old_cmds_data.pickle", "rb") as f:
            self.old_cmds = pickle.load(f)
        self.baseParser.Examination()

    def start(self):
        while True:
            cmds = [cmd for cmd in self.senderController.getCommands() if cmd not in self.old_cmds]
            _ = [self.commandController.executeCommand(cmd) for cmd in cmds]
            self.old_cmds.extend(cmds)

    def __del__(self):
        with open("data/old_cmds_data.pickle", "wb") as f:
            pickle.dump(self.old_cmds, f)
