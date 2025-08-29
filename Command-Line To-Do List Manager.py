import json
from datetime import datetime, timedelta
import os

FILE_NAME = "tasks.json"
def load_tasks():
    """Load tasks from file if available"""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
    status = "Pending"

    task = {"description": description, "due_date": due_date, "status": status}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!\n")
def view_tasks(tasks, filter_type="all"):
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n---- Task List ----")
    today = datetime.now().date()

    for idx, task in enumerate(tasks, 1):
        due_date = task["due_date"]
        status = task["status"]

        if filter_type == "completed" and status != "Completed":
            continue
        elif filter_type == "pending" and status != "Pending":
            continue
        elif filter_type == "due_soon":
            if not due_date:
                continue
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d").date()
                if due > today + timedelta(days=3):
                    continue
            except ValueError:
                continue

        print(f"{idx}. {task['description']} | Due: {due_date or 'N/A'} | Status: {status}")
    print("--------------------\n")
def mark_complete(tasks):
    view_tasks(tasks, "pending")
    try:
        task_num = int(input("Enter task number to mark complete: "))
        tasks[task_num - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("✅ Task marked as completed!\n")
    except (ValueError, IndexError):
        print("❌ Invalid task number!\n")
def edit_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to edit: "))
        task = tasks[task_num - 1]

        new_desc = input(f"Enter new description (or press Enter to keep '{task['description']}'): ")
        new_due = input(f"Enter new due date (YYYY-MM-DD) or press Enter to keep '{task['due_date']}': ")

        if new_desc:
            task["description"] = new_desc
        if new_due:
            task["due_date"] = new_due

        save_tasks(tasks)
        print("✏️ Task updated successfully!\n")
    except (ValueError, IndexError):
        print("❌ Invalid task number!\n")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed['description']}' deleted!\n")
    except (ValueError, IndexError):
        print("❌ Invalid task number!\n")
def main():
    tasks = load_tasks()

    while True:
        print("==== To-Do List Manager ====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View Pending Tasks")
        print("5. View Tasks Due Soon")
        print("6. Mark Task as Completed")
        print("7. Edit Task")
        print("8. Delete Task")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks, "all")
        elif choice == "3":
            view_tasks(tasks, "completed")
        elif choice == "4":
            view_tasks(tasks, "pending")
        elif choice == "5":
            view_tasks(tasks, "due_soon")
        elif choice == "6":
            mark_complete(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            print("Exiting... ✅ Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
