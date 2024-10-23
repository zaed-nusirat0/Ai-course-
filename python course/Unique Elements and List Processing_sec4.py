### Challenge 2: Unique Elements and List Processing
def Unique_number(list_number):
    """
    This function takes a list of numbers and returns the squares of all unique even numbers.
    
    Parameters:
    list_number (list): A list of integers.
    
    Returns:
    str: A formatted string that contains the squares of the unique even numbers.
    """
    # Convert the list to a set to remove duplicates and then back to a list
    set_number = list(set(list_number))
    
    # Create a list of squares of even numbers from the unique numbers
    squares_of_even_numbers = [num**2 for num in set_number if num % 2 == 0]
    
    # Return the result as a formatted string
    return f"(Squares of even numbers) : {squares_of_even_numbers}"

try:
    # Ask the user for the range of numbers they want to input
    range_list = int(input('Enter the number of range input : '.title()))
    
    # Collect the numbers from the user based on the range provided
    list_number = [int(input(f'Enter the number {i+1} of list : '.title())) for i in range(range_list)]
    
    # Call the function and print the result
    print(Unique_number(list_number))

# Handle potential errors (invalid input types or values)
except (TypeError, ValueError) as e:
    print(f"Found error {e}".title())
