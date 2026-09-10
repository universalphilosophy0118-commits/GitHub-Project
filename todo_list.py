tasks = []
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for task in tasks:
                print(task)
    elif choice == "3":
        task = input("Enter the task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")