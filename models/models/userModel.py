from models.models.baseModel import BaseModel


class UserModel(BaseModel):
    table_name = "users"
    table_headers = {"chat_id": "INTEGER", "service": "TEXT", "group_name": "TEXT"}
