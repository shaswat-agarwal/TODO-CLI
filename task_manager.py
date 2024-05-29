from datetime import datetime


# Add a new task
def add_task(tasks, save_tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high, medium, low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")

    # Validate due date format
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


# Remove a task
def remove_task(tasks, save_tasks):
    list_tasks(tasks)
    task_id = int(input("Enter the task ID to remove: "))
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task ID.")


# Mark a task as completed
def complete_task(tasks, save_tasks):
    list_tasks(tasks)
    task_id = int(input("Enter the task ID to mark as completed: "))
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")


# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(
            f"{idx}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}"
        )
