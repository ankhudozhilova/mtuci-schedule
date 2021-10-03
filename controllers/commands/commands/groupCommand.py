from controllers.commands.baseCommand import BaseCommand
from models.models.userModel import UserModel

class GroupCommand(BaseCommand):

    def __init__(self):
        self.db = UserModel()
        self.group = self.command['text'].replace('group ','').upper()
        self.tgId = self.command['chat_id']
        self.service = self.command['service']
        self.legalGroups = ['БВТ210' + str(i) for i in range(1,9)]

    def makeAnswer(self) -> None:

        data = self.db.read_data()
        data = list(filter(lambda x: self.tgId in x,data))
        if data or (self.group not in self.legalGroups):
            msg = 'Вы уже добавлены в базу данных или ввели неверное название группы'
        else:
            self.db.save_data(data = [
                self.tgId,
                self.service,
                self.group
            ])
            msg = 'Вы добавлены в базу данных'

        super(GroupCommand, self).makeAnswer(msg)
