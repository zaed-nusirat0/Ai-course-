
'''
Challenge 1: Implement a Contact Book

Description: Create a small program where users can add, delete, and view contacts in a text file. Each contact will have a name and phone number.

'''

def add_contact(path):  # Define function to add a contact
  '''This function is responsible for adding a new contact to the file at the specified path. 
  It collects three pieces of information from the user: name, phone number, and age. The name is taken as a string, while the phone number and age are
  expected to be integers. These details are then appended to the file. If invalid inputs (non-integer phone or age) are entered, a ValueError is raised and handled 
  with a message prompting the user to re-enter valid data.'''
  with open(path,'a') as file:  # Open the file in append mode to add new data at the end
    list_store=['Name','Phone','Age']  # List to store expected fields (name, phone, age)
    try:
      Name=input('Enter the name : '.title())  # Prompt the user to enter the name
      Phone=int(input('Enter the Phone : '.title()))  # Prompt the user to enter the phone number and convert to integer
      Age=int(input('Enter the Age : '.title()))  # Prompt the user to enter the age and convert to integer
      file.write(f'Name : {Name}\n')  # Write the name to the file
      file.write(f'Phone : {Phone}\n')  # Write the phone number to the file
      file.write(f'Age : {Age}\n')  # Write the age to the file
    except ValueError:  # Handle case when input is not an integer
            print("Invalid input: Phone and Age must be integers. Please try again.")  # Print error message for invalid input

def delete_contact(path):  # Define function to delete a contact

  '''This function deletes a contact from the file. It prompts the user to enter the name of the contact they wish to delete. 
  he function reads all the lines from the file and looks for the line that contains the given name. 
  If found, it skips the next three lines (name, phone, age) to effectively delete the contact. 
  The updated contact list is then written back to the file, overwriting the original content.

   '''
  with open(path,'r') as file:  # Open the file in read mode
    lines=file.readlines()  # Read all lines from the file
    name_input=input('Enter the name '.title())  # Prompt the user to enter the name to delete
    new_lines=[]  # Initialize a new list to store remaining lines
    i=0  # Initialize index to loop through the lines
    while i <len(lines):  # Loop through all lines
      if name_input in lines[i]:  # If the name is found in the current line
        print(f'contact {name_input}  successfully deleted'.title())
        i+=3  # Skip the next 3 lines (name, phone, age) to delete the contact
      else:
        new_lines.append(lines[i])  # Otherwise, add the current line to the new list
        i+=1  # Move to the next line
      with open(path,'w') as file:  # Open the file in write mode to overwrite with new content
        file.writelines(new_lines)  # Write the updated list of lines to the file

def view_contacts(path):  # Define function to view all contacts
   '''This function displays all the contacts stored in the file. It opens the file and reads its contents, printing them to the console. 
   If the file is not found at the given path, the function raises and catches a FileNotFoundError, 
   and prints the error message to inform the user.'''
   
   try:
    with open(path) as file:  # Open the file in read mode
      print(file.read())  # Print the content of the file
   except FileNotFoundError as e:  # Handle case when file is not found
    print(e)  # Print the error message

path=input('ENTER THE PATH IN SYSTEM '.title()).lower()  # Prompt the user to enter the file path and convert to lowercase
operation=['add','delete','view']  # List of supported operations
print(operation) # print the operations 
while True:  # Start an infinite loop
  choice=input('Enter operation '.title()).lower()  # Prompt the user to choose an operation and convert to lowercase
  if choice in operation:  # Check if the chosen operation is valid
    if choice=='add':  # If the user chooses 'add'
      add_contact(path)  # Call the add_contact function
    elif choice=='delete':  # If the user chooses 'delete'
      delete_contact(path)  # Call the delete_contact function
    elif choice=='view':  # If the user chooses 'view'
      view_contacts(path)  # Call the view_contacts function
    elif choice=='stop':  # If the user chooses 'stop'
      break  # Exit the loop
  else:
    print('no found operations '.title())  # If an invalid operation is entered, print an error message
    break  # Exit the loop
if choice=='stop':  # After the loop is stopped
  with open(path,'r') as file:  # Open the file in read mode
    print(file.read())  # Print the content of the file
