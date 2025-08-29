import json
import os

# Task class definition
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def edit(self, title=None, description=None, category=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category

# Save tasks to JSON file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from JSON file, ignoring unexpected fields
def load_tasks(filename='tasks.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        try:
            raw_tasks = json.load(f)
            clean_tasks = []
            for data in raw_tasks:
                clean_data = {
                    'title': data.get('title', ''),
                    'description': data.get('description', ''),
                    'category': data.get('category', ''),
                    'completed': data.get('completed', False)
                }
                clean_tasks.append(Task(**clean_data))
            return clean_tasks
        except json.JSONDecodeError:
            print("⚠️ Error reading tasks.json. Starting with an empty task list.")
            return []

# Display tasks in a readable format
def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\n📋 Current Tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        print(f"{i+1}. [{status}] {task.title} ({task.category})")
        print(f"    Description: {task.description}")

# Main CLI loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📝 Personal To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option (1–6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))
            print("✅ Task added successfully!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index].mark_completed()
                    print("✅ Task marked as completed.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '4':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to edit: ")) - 1
                if 0 <= index < len(tasks):
                    print("Leave blank to keep current value.")
                    new_title = input("New title: ")
                    new_description = input("New description: ")
                    new_category = input("New category: ")
                    tasks[index].edit(
                        title=new_title if new_title else None,
                        description=new_description if new_description else None,
                        category=new_category if new_category else None
                    )
                    print("✏️ Task updated.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '5':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    confirm = input(f"Are you sure you want to delete '{tasks[index].title}'? (y/n): ").lower()
                    if confirm == 'y':
                        deleted = tasks.pop(index)
                        print(f"🗑️ Deleted task: {deleted.title}")
                    else:
                        print("❌ Deletion cancelled.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '6':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
