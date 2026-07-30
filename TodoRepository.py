import sqlite3
from DTO.InputDTO import InputDTO, UpdateInputDTO
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

    def selectByName(self, title: str) -> List[SelectAllResponseDTO]:
        matchedTodos = self.conn.execute("""
            SELECT id, title, description, completed FROM todos WHERE title = ?
            """, (title,)).fetchall()
        return [SelectAllResponseDTO(todo[0], todo[1], todo[2], todo[3]) for todo in matchedTodos]

    def update_todo(self, id: int, update_dto: UpdateInputDTO) -> bool:
        # A NULL parameter leaves the existing column value in place,
        # so blank input from the caller means "don't update this field".
        cursor = self.conn.execute("""
            UPDATE todos SET
                title = COALESCE(?, title),
                description = COALESCE(?, description),
                completed = COALESCE(?, completed)
            WHERE id = ?
            """,
            (update_dto.title, update_dto.description, update_dto.completed, id))
        self.conn.commit()
        return cursor.rowcount > 0

    def disconnect(self):
        self.conn.close()