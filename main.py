from DI_container.Container import Container
from DTO.InputDTO import InputDTO

def main():
    
    container = Container()
    print("--------------------------------")
    print("Creating table...")
    repository = container.get_todo_repository()
    repository.create_table()
    print("Table created successfully")
    print("--------------------------------")

    while True:
        print("Welcome to the program")
        print("--------------------------------")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")
        print("--------------------------------")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Add a new task")
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")

            repository.add_todo(InputDTO(title, description))
            
            print("Task added successfully")

        elif choice == 2:
            allTodos : List[SelectAllResponseDTO] = repository.selectAll()

            for todo in allTodos:
                print(f"ID: {todo.id}, Title: {todo.title}, Description: {todo.description}, Completed: {todo.completed}")
            
            print("View all tasks")

        elif choice == 3:
            print("Update a task")
            title = input("Enter the title of the task (leave blank if you don't want to update): ").strip() or None
            description = input("Enter the description of the task (leave blank if you don't want to update): ").strip() or None
            
            raw_completed = input("Enter the completed status of the task: ").strip().lower()

            repository.update_todo(id, 
            UpdateInputDTO(
                title,
             description,
             x if raw_completed in ("0", "1") else None)
        
        elif choice == 4:
            print("Delete a task")
        elif choice == 5:
            print("Exicting CLI... for now")
            break
        elif choice == 6:
            print("Exit")
            repository.disconnect()
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()