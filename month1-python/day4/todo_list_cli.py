# Day 4 - To-Do List Application (CLI Version)
# Concepts: Lists, Loops, Conditionals

tasks = []

def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("⚠ No tasks available.")
        else:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("⚠ No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_number = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_number - 1)
                print(f"❌ Removed: {removed}")
            except (ValueError, IndexError):
                print("⚠ Invalid selection.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("⚠ Invalid option. Please choose 1-4.")