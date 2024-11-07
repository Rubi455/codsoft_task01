class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task number.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

# Instantiate ToDoList
todo_list = ToDoList()

def display_menu():
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Show Tasks")
    print("6. Exit")

def main():
    todo_list = ToDoList()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")  # Get user choice
        
        if choice == '1':  # Add Task
            task = input("Enter the task: ")  # Get task description from the user
            todo_list.add_task(task)
            print(f"Task '{task}' added.")
        
        elif choice == '2':  # Update Task
            try:
                index = int(input("Enter task number to update: "))  # Get task index
                new_task = input("Enter the new task: ")  # Get the new task description
                todo_list.update_task(index, new_task)
                print(f"Task number {index} updated to '{new_task}'.")
            except ValueError:
                print("Please enter a valid number for the task.")
        
        elif choice == '3':  # Delete Task
            try:
                index = int(input("Enter task number to delete: "))  # Get task index
                todo_list.delete_task(index)
                print(f"Task number {index} deleted.")
            except ValueError:
                print("Please enter a valid number for the task.")
        
        elif choice == '4':  # Mark Task as Completed
            try:
                index = int(input("Enter task number to mark as completed: "))  # Get task index
                todo_list.mark_completed(index)
                print(f"Task number {index} marked as completed.")
            except ValueError:
                print("Please enter a valid number for the task.")
        
        elif choice == '5':  # Show Tasks
            todo_list.display_tasks()
        
        elif choice == '6':  # Exit
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
