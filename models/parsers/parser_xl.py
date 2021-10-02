from models.parsers.parser_assistant import Assistant
from models.converts.baseParser import ExcelToDataBase


class Parser:

    def __init__(self):
        self.file = Assistant.file
        self.dictionary = Assistant.dictionary
        self.days = Assistant.days
        self.group_names = Assistant.group_names
        self.group = Assistant.group
        self.name_group = Assistant.name_group

        Parser.Examination(self)

    def Logic(self):
        index_line, self.group = 12, self.group_names.index(self.group) + 3
        for num in range(6):
            schedule, count = [], 0
            while index_line < 132:
                lines_1_2 = list(
                    self.file[index_line + i][self.group - (Parser.Union(self, index_line))].value for i in
                    range(0, 2))
                lines_3_4 = list(
                    self.file[index_line + i][self.group - (Parser.Union(self, index_line + 2))].value for i in
                    range(2, 4))
                if count == 5:
                    break

                if lines_1_2[0] is None and lines_1_2[1] is not None and lines_3_4[0] is None:
                    schedule.append('СРС')
                    break
                if lines_1_2[0] is None and lines_1_2[1] is None:
                    schedule.append('1 Пары нет')
                if lines_1_2[0] is None and lines_1_2[1] is not None and lines_3_4[0] is not None and lines_3_4[1] \
                        is None:
                    schedule.append('0 {0} {1}'.format(lines_1_2[1], lines_3_4[0]))
                if lines_1_2[0] is not None and lines_1_2[1] is not None:
                    if lines_3_4[0] is not None and 'ФИЗИЧЕСКАЯ' not in lines_3_4[0] and lines_3_4[1] is None:
                        schedule.append('0 {0}! {1}! {2}'.format(lines_1_2[0], lines_1_2[1], lines_3_4[0]))
                    else:
                        schedule.append('1 {0} {1}'.format(lines_1_2[0], lines_1_2[1]))
                if lines_3_4[0] is not None and lines_3_4[1] is not None:
                    if lines_1_2[0] is None and lines_1_2[1] is not None:
                        schedule.append('0 {0}! {1}! {2}'.format(lines_1_2[1], lines_3_4[0], lines_3_4[1]))
                    else:
                        schedule.append('2 {0} {1}'.format(lines_3_4[0], lines_3_4[1]))
                if lines_3_4[0] is None and lines_3_4[1] is None:
                    schedule.append('2 Пары нет')

                index_line += 4
                count += 1
            self.dictionary[self.days[0]] = schedule
            del self.days[0]

        ExcelToDataBase()
        self.name_group.clear()

    def Examination(self):
        for group in self.group_names:
            self.group = group
            self.name_group.append(group)
            for keys in self.dictionary:
                self.dictionary[keys] = []
                self.days.append(keys)
            Parser.Logic(self)

    def Union(self, index_line):
        cell = self.file.cell(row=index_line, column=int(self.group) + 1)
        if type(cell).__name__ == 'MergedCell':
            return 1
        return 0


Parser()  # Убрать !!!
