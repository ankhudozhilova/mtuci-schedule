from models.models.baseModel import BaseModel


class TimeTableModel(BaseModel):
    table_name = "timetable"
    table_headers = {"evens": "int", "lesson_type": "int", "day_name": "TEXT", "subject": "TEXT",
                     "group_name": "TEXT", "tutor": "TEXT", "rooms": "TEXT"}
