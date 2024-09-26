# A simple and optimized To-Do List application

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    menu = """
    --- To-Do List Menu ---
    1. View tasks
    2. Add a task
    3. Remove a task
    4. Update a task
    5. Exit
    """
    print(menu)

def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nYour to-do list is empty!")

def add_task():
    task = input("\nEnter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def get_task_number(action):
    view_tasks()
    if not tasks:
        return None
    
    try:
        task_num = int(input(f"\nEnter the task number to {action}: "))
        if 1 <= task_num <= len(tasks):
            return task_num - 1
        else:
            print("Invalid task number!")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def remove_task():
    task_index = get_task_number("remove")
    if task_index is not None:
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")

def update_task():
    task_index = get_task_number("update")
    if task_index is not None:
        new_task = input("Enter the updated task: ").strip()
        if new_task:
            tasks[task_index] = new_task
            print(f"Task {task_index + 1} updated successfully!")
        else:
            print("Task cannot be empty!")

def main():
    actions = {
        '1': view_tasks,
        '2': add_task,
        '3': remove_task,
        '4': update_task,
        '5': lambda: print("Exiting the To-Do List application. Goodbye!")
    }
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            actions[choice]()
            break
        action = actions.get(choice)
        
        if action:
            action()
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
