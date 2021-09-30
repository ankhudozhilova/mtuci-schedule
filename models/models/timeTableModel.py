from models.models.baseModel import BaseModel


class TimeTableModel(BaseModel):
    table_name = "timetable"
    table_headers = {"evens": "int", "lesson_type": "int", "day_name": "text", "subject": "text",
                     "group_name": "text", "tutor": "text", "rooms": "text"}
