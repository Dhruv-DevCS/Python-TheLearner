import os

TASKS_FILE = "C:\\Users\\ADMIN\\Desktop\\PYTHON\\Quick Projects\\To-Do List\\tasks.txt"
DONE_FILE = "C:\\Users\\ADMIN\\Desktop\\PYTHON\\Quick Projects\\To-Do List\\done_tasks.txt"

def load_tasks(filename):
    """Load tasks from file"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(filename, tasks):
    """Save tasks to file"""
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks():
    """Display all pending tasks"""
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print("\nNo pending tasks!")
        return
    print("\n--- Pending Tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    """Add a new task"""
    task = input("\nEnter task: ").strip()
    if task:
        tasks = load_tasks(TASKS_FILE)
        tasks.append(task)
        save_tasks(TASKS_FILE, tasks)
        print("Task added!")

def remove_task():
    """Remove a task"""
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print("\nNo tasks to remove!")
        return
    view_tasks()
    try:
        idx = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            save_tasks(TASKS_FILE, tasks)
            print("Task removed!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def mark_done():
    """Mark task as done"""
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print("\nNo tasks to mark!")
        return
    view_tasks()
    try:
        idx = int(input("\nEnter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            done_tasks = load_tasks(DONE_FILE)
            done_tasks.append(tasks[idx])
            save_tasks(DONE_FILE, done_tasks)
            tasks.pop(idx)
            save_tasks(TASKS_FILE, tasks)
            print("Task marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def view_done():
    """Display all done tasks"""
    done_tasks = load_tasks(DONE_FILE)
    if not done_tasks:
        print("\nNo completed tasks!")
        return
    print("\n--- Completed Tasks ---")
    for i, task in enumerate(done_tasks, 1):
        print(f"{i}. {task}")

def clear_done():
    """Clear all done tasks"""
    save_tasks(DONE_FILE, [])
    print("Done tasks cleared!")

def main():
    """Main menu"""
    while True:
        print("\n=== TODO LIST ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. View done tasks")
        print("6. Exit")
        print("7. Clear done tasks")
        
        choice = input("\nChoose option (1-7): ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            view_done()
        elif choice == "6":
            print("Goodbye!")
            break
        elif choice == "7":
            clear_done()
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()