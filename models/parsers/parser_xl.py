from models.parsers.parser_assistant import Assistant


class Parser:
    group = None

    def __init__(self):
        self.file = Assistant.file
        self.dictionary = Assistant.dictionary
        self.days = Assistant.days
        self.group_names = Assistant.group_names

        Parser.Examination(self)

    def setGroup(self, group: str) -> None:
        self.group = group

    def Logic(self):
        index_line, self.group = 12, self.group_names.index(self.group) + 3
        for num in range(6):
            sched, count = '', 0
            while index_line < 132:
                lines_1_2 = list(
                    self.file[index_line + i][self.group - (Parser.Union(self, index_line))].value for i in
                    range(0, 2))
                lines_3_4 = list(
                    self.file[index_line + i][self.group - (Parser.Union(self, index_line + 2))].value for i in
                    range(2, 4))
                if count == 5:
                    break
                if lines_1_2[0] is None and lines_1_2[1] is None:
                    sched += 'Неч. Пары нет\n'
                if lines_1_2[0] is not None and lines_1_2[1] is not None:
                    sched += 'Неч. {0} {1}\n'.format(lines_1_2[0], lines_1_2[1])
                if lines_1_2[0] is None and lines_1_2[1] is not None:
                    sched += 'Всегда {0} {1}\n---------------\n'.format(lines_1_2[1], lines_3_4[0])
                elif lines_3_4[0] is not None and lines_3_4[1] is not None:
                    sched += 'Чет. {0} {1}\n---------------\n'.format(lines_3_4[0], lines_3_4[1])
                if lines_3_4[0] is None and lines_3_4[1] is None:
                    sched += 'Чет. Пары нет\n---------------\n'
                index_line += 4
                count += 1
            self.dictionary[self.days[0]] = '{0}:\n---------------\n'.format(self.days[0].title()) + str(sched)
            Parser.DEL(self)

    @staticmethod
    def Error():
        exit()

    def Examination(self):
        if self.group in self.group_names:
            Parser.Logic(self)
        else:
            Parser.Error()

    def DEL(self):
        del self.days[0]

    def Union(self, index_line):
        cell = self.file.cell(row=index_line, column=int(self.group) + 1)
        if type(cell).__name__ == 'MergedCell':
            return 1
        return 0

    def getDay(self, day: str):
        return self.dictionary[day]
