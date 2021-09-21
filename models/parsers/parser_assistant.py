from openpyxl import load_workbook
import os


def Adding(file, group_names):
    for a in range(3, 19):
        group_names.append(file[11][a].value)


class Assistant:
    data = (str(os.path.abspath('Schedule.xlsx'))).replace('parsers', 'data')
    file = load_workbook(data).active
    dictionary = {'monday': [],
                  'tuesday': [],
                  'wednesday': [],
                  'thursday': [],
                  'friday': [],
                  'saturday': []}
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    group_names = []

    Adding(file, group_names)
