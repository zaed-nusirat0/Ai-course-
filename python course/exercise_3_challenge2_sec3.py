'''Challenge 2: To-Do List Manager

Description: Write a program that allows users to add tasks to a to-do list, mark them as completed, and save the to-do list to a file.

Hints:

Each task could be saved in the format "Task,Completed" in the file (e.g., "Wash dishes,False").
Allow reading, adding, and updating tasks.'''

# Function to add a task to the to-do list
def add_tasks(path):
    # Open the file in write mode to overwrite existing tasks
    with open(path, 'w') as file:
        # Prompt the user to input the task
        input_tasks = input('Enter the task: '.title()).lower()  # Convert to lowercase for consistency
        # Ask the user if the task is completed (True/False)
        completed_tasks = input('Is the task completed? (True/False): '.title()).lower()
        # Write the task and its status (True/False) to the file
        file.write(f'{input_tasks} {completed_tasks}\n')

# Function to view all tasks in the to-do list
def view_tasks(path):
    # Open the file in read mode
    with open(path, 'r') as file:
        # Print all tasks in the file
        print(file.read())

# Function to edit an existing task (mark it as completed if it's not)
def edit_task(path):
    # Open the file in read mode and read all lines
    with open(path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        # Prompt the user to enter the task they want to edit
        edit_task = input('Enter the task to edit: '.title()).lower()
        new_lines = []  # List to store the modified tasks
        # Iterate over each line (task) in the file
        for line in lines:
            if line.strip() == ' ':  # Skip empty lines
                continue
            if edit_task in line:  # If the task to edit is found
                # Split the task and its status (True/False)
                task_parts = line.rsplit(' ', 1)
                # If the task's status is 'false', mark it as 'true'
                if 'false' in task_parts[1]:
                    task_parts[1] = 'true'
                    # Reconstruct the line with the updated status
                    line = ' '.join(task_parts)
                # Add the updated task to the new list
                new_lines.append(line)
            else:
                # If no edit is needed, add the original task to the new list
                new_lines.append(line)
        
        # Write the updated tasks back to the file
        with open(path, 'w') as file:
            file.writelines(new_lines)

# Main program loop: Choose between add, view, or edit operations
operations = ['add', 'view', 'edit']
# Prompt the user to enter the file path for the to-do list
path = input('Enter the path to your to-do list file: '.title())
while True:
    # Ask the user for the operation they want to perform
    choice = input('Enter the operation (add, view, edit): '.title())
    if choice in operations:
        if choice == 'add':
            # Call add_tasks() if the user wants to add a task
            add_tasks(path)
        elif choice == 'edit':
            # Call edit_task() if the user wants to edit a task
            edit_task(path)
        else:
            # Call view_tasks() if the user wants to view the tasks
            view_tasks(path)
    else:
        # If the operation is not found, inform the user and break the loop
        print('The operation not found.'.title())
        break

# Optional: If the user types 'stop', print the final contents of the file
if choice == 'stop':
    with open(path, 'r') as file:
        print(file.read())
