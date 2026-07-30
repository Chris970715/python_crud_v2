import sqlite3
from DTO.InputDTO import InputDTO
from DTO.ResponseDTO import SelectAllResponseDTO
from typing import List

class TodoRepository:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
    
    def create_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            ) 
            """
        )
    
    def add_todo(self, input_dto: InputDTO):
        self.conn.execute (("""
         INSERT INTO todos (title, description, completed) VALUES (?, ?, ?)
         """), 
         (input_dto.title,
          input_dto.description,
           input_dto.completed))
        self.conn.commit()
    
    def selectAll(self) -> List[SelectAllResponseDTO]:
        allTodos = self.conn.execute("""
            SELECT id, title, description, completed FROM todos
            """).fetchall()
        return [SelectAllResponseDTO(todo[0], todo[1], todo[2], todo[3]) for todo in allTodos]
    
    def disconnect(self):
        self.conn.close()