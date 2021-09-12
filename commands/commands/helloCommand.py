from commands.baseCommand import BaseCommand


class HelloCommand(BaseCommand):

    def makeAnswer(self) -> None:
        msg = "Привет студент из Мтуси, чтобы увидеть расписание, пожалуйста введи команду: '/group [name]', " \
              "где name = твоя группа, например: '/group бтв2102' "
        super(HelloCommand, self).makeAnswer(msg)