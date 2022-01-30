import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchall=False, commit=False, fetchone=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name VARCHAR(255),
            email VARCHAR(255),
            language VARCHAR(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} =?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):

        sql = """
        INSERT INTO users(id, Name) VALUES(?,?)
        """
        self.execute(sql, parameters=(id, name), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        result = self.execute(sql, fetchall=True)
        return [x[0] for x in result]

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE"
        sql, parameters = self.format_args(sql, kwargs)
        return  self.execute(sql, parameters=parameters, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchall=True)

    def update_user_email(self, email, id):
        sql = f"""
        UPDATE Users SET email = ? WHERE id = ?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def print_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

def logger(statement):
    print(f"""
Executing:
{statement}
""")
