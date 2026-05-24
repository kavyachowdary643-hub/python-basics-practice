tasks = []
def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")
def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")