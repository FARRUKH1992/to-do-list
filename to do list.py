# create CLI
# display welcome message
# implement addind, viewing, marking, delete, amd quit app
# allow user to interract
# implement input validation
# error handling
# orginize the code
# test and debug






import sys

def display_menu():
    """Display the menu options."""
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(task_list):
    """Add a new task to the task list."""
    try:
        title = input("Enter the task title: ").strip()
        if title == "":
            raise ValueError("Task title cannot be empty.")
        task_list.append({"title": title, "status": "Incomplete"})
        print(f"Task '{title}' added.")
    except ValueError as e:
        print(f"Error: {e}")

def view_tasks(task_list):
    """View all tasks with their status."""
    if not task_list:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for i, task in enumerate(task_list):
            print(f"{i + 1}. {task['title']} - {task['status']}")

def mark_task_complete(task_list):
    """Mark a task as complete."""
    try:
        view_tasks(task_list)
        task_number = int(input("Enter the task number to mark as complete: "))
        if task_number < 1 or task_number > len(task_list):
            raise IndexError("Task number out of range.")
        task_list[task_number - 1]['status'] = "Complete"
        print(f"Task {task_number} marked as complete.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def delete_task(task_list):
    """Delete a task from the list."""
    try:
        view_tasks(task_list)
        task_number = int(input("Enter the task number to delete: "))
        if task_number < 1 or task_number > len(task_list):
            raise IndexError("Task number out of range.")
        deleted_task = task_list.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def main():
    """Main function to run the To-Do List Application."""
    task_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                add_task(task_list)
            elif choice == 2:
                view_tasks(task_list)
            elif choice == 3:
                mark_task_complete(task_list)
            elif choice == 4:
                delete_task(task_list)
            elif choice == 5:
                print("Quitting the application.")
                break
            else:
                print("Invalid option. Please choose between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        finally:
            print("Thank you for using the To-Do List App.")

if __name__ == "__main__":
    main()