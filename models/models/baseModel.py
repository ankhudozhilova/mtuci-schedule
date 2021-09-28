import sqlite3 as sql


class BaseModel:
    table_name = ""
    table_headers = {}
    bd_name = "data/database.db"

    def __init__(self):
        self.conn = sql.connect(self.bd_name)
        self.cur = self.conn.cursor()

        sql_request = f"CREATE TABLE IF NOT EXISTS {self.table_name}(id INTEGER PRIMARY KEY, " \
                      f"{', '.join([f'{k} {v}' for k, v in self.table_headers.items()])})"

        self.cur.execute(sql_request)
        self.conn.commit()

        data = self.cur.execute(f"SELECT * FROM {self.table_name}").fetchall()
        if not data:
            self.id = 0
        else:
            self.id = int(data[-1][0]) + 1

    def _convert_data(self, data: list) -> list:
        for i, data_type in enumerate(self.table_headers.values()):
            if data_type == "TEXT":
                data[i] = f"\"{data[i]}\""
            elif data[i] is None:
                data[i] = "NULL"
            else:
                data[i] = str(data[i])
        return data

    def save_data(self, data: list) -> None:
        sql_request = f"INSERT INTO {self.table_name} VALUES" \
                      f"({self.id}, {', '.join(self._convert_data(data))})"
        self.cur.execute(sql_request)
        self.conn.commit()

        self.id += 1

    def read_data(self) -> list:
        return self.cur.execute(f"SELECT * FROM {self.table_name}").fetchall()

    def remove_data(self, condition: list) -> None:
        sql_request = f"DELETE FROM {self.table_name} WHERE {str(condition[0])} = {str(condition[1])}"

        self.cur.execute(sql_request)
        self.conn.commit()

    def __del__(self):
        self.conn.close()