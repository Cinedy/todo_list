from models import ToDoSqlService

def main():
    todo_list = ToDoSqlService()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            task_name = input("Enter the task: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            tasks = todo_list.view_tasks()
            if not tasks:
                print("No tasks created yet!")
            else:
                for task_id, name, done in tasks:
                    status = "Done" if done else "Not Done"
                    print(f"{task_id}. {name} - {status}")
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            todo_list.mark_done(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")