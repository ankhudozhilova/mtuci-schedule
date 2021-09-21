from models.models.baseModel import BaseModel


class TimeTableModel(BaseModel):
    table_name = "timetable"
    table_headers = {"evens": "int", "ltype": "int", "stream": "int", "dow": "text", "subject": "text",
                    "group_name": "text", "tutor": "text", "rooms": "text", "timel": "text"}
