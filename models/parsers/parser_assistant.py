from openpyxl import load_workbook
import os


def Adding(file, group_names):
    for a in range(3, 19):
        group_names.append(file[11][a].value)


class Assistant:
    data = (str(os.path.abspath('Schedule.xlsx'))).replace('parsers', 'data').replace('models', '')
    file = load_workbook(data).active
    dictionary = {'monday': [],
                  'tuesday': [],
                  'wednesday': [],
                  'thursday': [],
                  'friday': [],
                  'saturday': []}
    days = []
    group_names = []
    name_group = []
    group = None

    Adding(file, group_names)
