# Simple Terminal To Do List v1
# CAPS LOCK DAVE 8/26/2023

def display_menu():
    """Display the available commands."""
    print("\nMENU:")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Remove Item from To-Do List")
    print("4. Mark Item as Done")
    print("5. Exit")

def view_tasks(tasks):
    """Display all the tasks."""
    if not tasks:
        print("To-Do List is empty!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to remove: "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num-1)
        print(f"'{removed}' has been removed from the list.")
    else:
        print("Invalid task number.")

def mark_done(tasks):
    """Mark a task as DONE."""
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num-1] = f"DONE // {tasks[task_num-1]}"
        print(f"Task {task_num} has been marked as done.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
