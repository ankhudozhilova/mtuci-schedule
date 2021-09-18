from commands.baseCommand import BaseCommand
from commands.commands.errorCommand import ErrorCommand
from commands.commands.helloCommand import HelloCommand

class CommandController:
    cmds = {
        "hello": HelloCommand(),
        "error": ErrorCommand(),
        "start": HelloCommand(),
    }

    @staticmethod
    def cleanCommand(text: str) -> str:
        return text.replace("/", "")

    def processingCommand(self, cmd: BaseCommand, command: dict) -> None:
        cmd.setCommand(command)
        cmd.makeAnswer()
        cmd.sendAnswer()

    def executeCommand(self, command: dict) -> None:
        cmd = self.cmds.get(self.cleanCommand(command["text"]))
        if cmd:
            self.processingCommand(cmd, command)
        else:
            self.processingCommand(self.cmds.get("error"), command)
