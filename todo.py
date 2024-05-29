from file_handler import load_tasks, save_tasks
from task_manager import add_task, remove_task, complete_task, list_tasks


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks, save_tasks)
        elif choice == "2":
            remove_task(tasks, save_tasks)
        elif choice == "3":
            complete_task(tasks, save_tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
