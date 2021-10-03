from controllers.commands.baseCommand import BaseCommand
import unicodedata

class HelpCommand(BaseCommand):

    def makeAnswer(self) -> None:
        msg = """
        /start - знакомство
        /help - список комманд
        /group - название группы
        /today - расписание на сегодня (команда не готова)
        /tommorow - расписание на зватра (команда не готова)
              """
        super(HelpCommand, self).makeAnswer(msg)