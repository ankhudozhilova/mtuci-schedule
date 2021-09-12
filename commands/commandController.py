from commands.commands.helloCommand import HelloCommand


class CommandController:
    cmds = {
        "hello": HelloCommand()
    }

    @staticmethod
    def cleanCommand(text: str) -> str:
        return text.replace("/", "")

    def executeCommand(self, command):
        cmd = self.cmds.get(self.cleanCommand(command["text"]))
        if cmd:
            cmd.setCommand(command)
            cmd.makeAnswer()
            cmd.sendAnswer()
