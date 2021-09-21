from controllers.commands.baseCommand import BaseCommand


class ErrorCommand(BaseCommand):

    def makeAnswer(self) -> None:
        msg = "такой комманды нету, пожалуйста, обратитесь к команде '/help'"
        super(ErrorCommand, self).makeAnswer(msg)