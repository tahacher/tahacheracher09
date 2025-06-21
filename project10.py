tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task" +str(task) + "added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(str(i) + ": " + task)

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        removed_task = tasks.pop(task_num)
        print("Task" + str(removed_task) + "deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def menu():
    while True:
        print("\n1. Add Task  2. View Tasks  3. Delete Task  4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

