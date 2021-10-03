from controllers.commands.baseCommand import BaseCommand


class StartCommand(BaseCommand):

    def makeAnswer(self) -> None:
        msg = """
        Привет !
        Я бот, который поможет тебе узнать 
        актуальное расписание твоей группы.
        Введи /help, чтобы узнать полный список возможностей.
        """
        super(StartCommand, self).makeAnswer(msg)