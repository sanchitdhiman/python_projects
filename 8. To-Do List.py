from datetime import date

# Task class represents a single task with name, priority, and due date
class Task:
    def __init__(self, name, priority="LOW", due_date=None):
        self.name = name  # Name of the task
        self.priority = priority  # Priority level (HIGH/MEDIUM/LOW)
        self.due_date = due_date  # Due date of the task
    
    # Change the name of the task
    def change_name(self, name):
        self.name = name

    # Change the priority of the task
    def change_priority(self, priority):
        self.priority = priority
    
    # Change the due date of the task
    def change_due_date(self, due_date):
        self.due_date = due_date


# Utility function to validate date input in DD/MM/YYYY format
def validate_date(date_str):
    try:
        # Convert string to date object
        date_obj = date(int(date_str[6:]), int(date_str[3:5]), int(date_str[:2]))
        # Ensure the date is not in the past
        if date_obj < date.today():
            return None
    except ValueError:
        return None
    return date_obj


# Utility function to validate priority input (HIGH/MEDIUM/LOW)
def validate_priority(priority):
    return priority.upper() in {"HIGH", "MEDIUM", "LOW"}


# Profile class represents the user's to-do list
class Profile:
    def __init__(self):
        self.pending = {}  # Dictionary to store pending tasks
        self.completed = {}  # Dictionary to store completed tasks
        self.task_id = 1  # Task ID counter for unique identification

    # Add a new task to the pending list
    def add_task(self, task):
        self.pending[self.task_id] = task  # Add task to the dictionary
        self.task_id += 1  # Increment task ID
        print("\nTask added successfully!")

    # General function to display tasks (used for both pending and completed)
    def view_tasks(self, tasks, status):
        if tasks:  # Check if there are tasks to display
            print(f"\n{status.title()} Tasks:")
            print("\nID - Name - Priority - Due Date")
            for id, task in tasks.items():  # Loop through tasks and display details
                print(f"{id} - {task.name} - {task.priority} - {task.due_date}")
        else:
            print(f"\nNo {status.lower()} tasks!")  # Message if no tasks are available

    # View only pending tasks
    def view_pending_tasks(self):
        self.view_tasks(self.pending, "Pending")

    # Display both pending and completed tasks
    def display_tasks(self):
        self.view_tasks(self.pending, "Pending")
        self.view_tasks(self.completed, "Completed")

    # Update a property (name, priority, or due date) of a specific task
    def update_task(self, id, prop, new_value):
        if id not in self.pending:  # Check if the task ID exists in pending
            print("\nTask not found!")
            return

        if prop == 1:  # Update name
            self.pending[id].change_name(new_value)
            print("\nName changed successfully!")
        elif prop == 2:  # Update priority
            if not validate_priority(new_value):  # Validate priority
                print("\nInvalid Priority! Task not updated.")
                return
            self.pending[id].change_priority(new_value.upper())
            print("\nPriority changed successfully!")
        elif prop == 3:  # Update due date
            date_obj = validate_date(new_value)  # Validate date
            if date_obj is None:
                print("\nInvalid Date! Task not updated.")
                return
            self.pending[id].change_due_date(date_obj)
            print("\nDue date changed successfully!")

    # Remove a task from the pending list
    def remove_task(self, id):
        if id not in self.pending:  # Check if the task ID exists
            print("\nTask not found!")
            return
        del self.pending[id]  # Remove task from the dictionary
        print("\nTask removed successfully!")

    # Mark a pending task as completed
    def mark_as_completed(self, id):
        if id not in self.pending:  # Check if the task ID exists
            print("\nTask not found!")
            return
        self.completed[id] = self.pending[id]  # Move task to completed dictionary
        del self.pending[id]  # Remove task from pending dictionary
        print("\nTask marked as completed!")


# Main Program: Handles the user interaction and performs operations
print("Welcome to To-Do List!")  # Initial greeting

# Create a user profile for managing tasks
user = Profile()
start = True  # Variable to control the main loop

# Main loop for user interaction
while start:
    # Display available operations
    print("""\nAvailable Operations:
    1. Add Task
    2. View Tasks
    3. Update Task
    4. Remove Task
    5. Mark a task as Completed""")

    # Prompt user to select an operation
    try:
        action = int(input("\nEnter the operation you want to perform (1/2/3/4/5): "))
        if action < 1 or action > 5:
            print("\nInvalid Operation! Please choose between 1 and 5.")
            continue
    except ValueError:
        print("\nInvalid Input! Please enter a number.")
        continue

    # Add a new task
    if action == 1:
        name = input("\nEnter the name of the task: ")
        priority = input("Enter the priority of the task (HIGH/MEDIUM/LOW): ").upper()
        if not validate_priority(priority):  # Validate priority
            print("\nInvalid Priority! Task not created.")
            continue
        due_date = input("Enter the due date of the task (DD/MM/YYYY): ")
        date_obj = validate_date(due_date)  # Validate date
        if date_obj is None:
            print("\nInvalid Date! Task not created.")
            continue

        # Create and add the new task
        new_task = Task(name, priority, date_obj)
        user.add_task(new_task)

    # View all tasks (pending and completed)
    elif action == 2:
        user.display_tasks()

    # Update a task
    elif action == 3:
        user.view_pending_tasks()  # Display pending tasks
        try:
            id = int(input("\nEnter the ID of the task you want to update: "))
        except ValueError:
            print("\nInvalid ID! Please enter a number.")
            continue
        print("\nYou can change only one property at a time.")
        print("\n1. Name\n2. Priority\n3. Due Date")
        try:
            prop = int(input("Which property do you want to change? (1/2/3): "))
            if prop not in {1, 2, 3}:
                print("\nInvalid Property! Choose 1, 2, or 3.")
                continue
        except ValueError:
            print("\nInvalid Input! Please enter a number.")
            continue

        new_value = input("\nEnter the new value: ")
        user.update_task(id, prop, new_value)

    # Remove a task
    elif action == 4:
        user.view_pending_tasks()  # Display pending tasks
        try:
            id = int(input("\nEnter the ID of the task you want to remove: "))
        except ValueError:
            print("\nInvalid ID! Please enter a number.")
            continue
        user.remove_task(id)

    # Mark a task as completed
    elif action == 5:
        user.view_pending_tasks()  # Display pending tasks
        try:
            id = int(input("\nEnter the ID of the task you want to mark as completed: "))
        except ValueError:
            print("\nInvalid ID! Please enter a number.")
            continue
        user.mark_as_completed(id)

    # Ask the user if they want to continue
    again = input("\nDo you want to perform another operation? (Y/N): ").lower()
    if again != 'y':  # Exit the program if the user enters 'n'
        start = False