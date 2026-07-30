from TodoRepository import TodoRepository

class Container:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance._todo_repository = None
            cls._instance._db_name = "todo.db"
        return cls._instance
    
    # Get the todo_repository instance
    def get_todo_repository(self) -> TodoRepository:
        if self._todo_repository is None:
            self._todo_repository = TodoRepository(self._db_name)
        return self._todo_repository

    # Get the todo_service instance

    # Get the todo_controller instance
    

    