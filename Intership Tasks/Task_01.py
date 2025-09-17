# to_do_list.py  Task_01

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter new task: ")
    tasks.append(task)
    print("Task added!")
def remove_task():
    show_tasks()
    try:
        task_no = int(input("\nEnter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
