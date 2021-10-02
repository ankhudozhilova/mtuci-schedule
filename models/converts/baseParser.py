from models.parsers.parser_assistant import Assistant


class ExcelToDataBase:
    evens = lesson_type = day_name = subject = group_name = tutor = rooms = None

    def __init__(self):
        self.dictionary = Assistant.dictionary
        self.group = Assistant.group
        self.name_group = Assistant.name_group

        ExcelToDataBase.OverTake(self)

    def OverTake(self):
        for key in self.dictionary:
            day = self.dictionary[key]

            ExcelToDataBase.TakeTurns(self, day, key)

    def TakeTurns(self, day, key):
        self.group_name = self.name_group[0]
        self.day_name = key.title()
        for element in day:
            element = ' '.join(element.lower().split())
            if element[0] == 'с':
                self.subject = 'СРС'
            else:
                self.evens = int(element[0])
                element = element[2:]
                if 'пары нет' in element:
                    self.subject = 'Пары нет'
                else:
                    if 'пр.з.' in element:
                        self.lesson_type = 2
                        element = element.replace('пр.з.', '')
                    if 'лек.' in element:
                        self.lesson_type = 1
                        element = element.replace('лек.', '')
                    if 'лаб.' in element:
                        self.lesson_type = 3
                        element = element.replace('лаб.', '')
                    element = ' '.join(element.lower().split())
                    if 'ауд.' in element:
                        if '!' in element:
                            element = element.split(sep='!')
                            self.subject = element[0].title()
                            if 'ауд.' in element[1]:
                                self.rooms = element[1].title()
                                self.tutor = element[2].title()
                            if 'ауд.' in element[2]:
                                self.rooms = element[2].title()
                                self.tutor = element[2].title()
                        else:
                            self.rooms = element[element.index('ауд.'):].title()
                            element = element.replace(element[element.index('ауд.'):], '')
                            if 'доц.' in element:
                                self.tutor = element[element.index('доц.'):].title()
                                element = element.replace(element[element.index('доц.'):], '')
                            if 'ст.пр.' in element:
                                self.tutor = element[element.index('ст.пр.'):].title()
                                element = element.replace(element[element.index('ст.пр.'):], '')
                            if 'проф.' in element:
                                self.tutor = element[element.index('проф.'):].title()
                                element = element.replace(element[element.index('проф.'):], '')
                            if 'попов а.п. ' in element:
                                self.tutor = element[element.index('попов а.п. '):].title()
                                element = element.replace(element[element.index('попов а.п. '):], '')
                            self.subject = element.title()
                    else:
                        self.subject = element.replace('!', '').title()
            collection = [self.evens, self.lesson_type, self.day_name, self.subject, self.group_name, self.tutor,
                          self.rooms]
            print(collection)  # Убрать !!!
            self.evens = self.lesson_type = self.subject = self.tutor = self.rooms = None
