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
            element = element.lower()
            self.evens = int(element[0])
            element = element.replace('{0} '.format(element[0]), '')
            if 'пары нет' in element:
                self.subject = 'Пары нет'
            else:
                if 'ауд.' in element:
                    self.rooms = element[element.index('ауд.'):]
                    element = element.replace('{0}'.format(element[element.index('ауд.'):]), '')
                if 'пр.з.' in element:
                    self.lesson_type = 2
                    element = element.replace('пр.з.', ',')
                if 'лаб.' in element:
                    self.lesson_type = 3
                    element = element.replace('лаб.', ',')
                if 'лек.' in element:
                    self.lesson_type = 1
                    element = element.replace('лек.', ',')
                subject_tutor = ' '.join(element.split()).split(sep=',')
                self.subject = subject_tutor[0].title().strip()
                if self.subject == 'Срс None':
                    self.subject = 'СРС'
                if len(subject_tutor) == 2:
                    if subject_tutor[1] != '':
                        self.tutor = subject_tutor[1].title().strip()
            collection = [self.evens, self.lesson_type, self.day_name, self.subject, self.group_name, self.tutor,
                          self.rooms]
            print(collection)  # Убрать !!!
            if self.subject == 'СРС':
                break
            self.evens = self.lesson_type = self.subject = self.tutor = self.rooms = None
