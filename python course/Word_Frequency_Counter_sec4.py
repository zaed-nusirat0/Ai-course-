''' Challenge 1: Word Frequency Counter
Write a program that takes a paragraph of text from the user and counts the frequency of each word using a **dictionary**.'''
def Word_Frequency_Counter(words):
    """
    This function takes a string of words and returns the frequency of each word.
    
    Parameters:
    words (str): A string containing words separated by spaces.
    
    Returns:
    str: A formatted string that shows the word frequency as a dictionary.
    """
    # Initialize an empty dictionary to store the frequency of each word
    Frequency_Counter = {}
    
    # Split the input string into words and count their occurrences
    for word in words.split():
        if word not in Frequency_Counter:
            # If the word is not in the dictionary, add it with a count of 1
            Frequency_Counter[word] = 1
        else:
            # If the word is already in the dictionary, increment its count
            Frequency_Counter[word] += 1
    
    # Return the frequency counter dictionary as part of a formatted string
    return f"Word Frequency Counter : {Frequency_Counter}"

# Continuous loop to take input from the user until 'stop' is entered
while True:
    Input = input('Enter the words in system : '.title())
    if Input != 'stop':
        # Call the Word_Frequency_Counter function and print the result
        print(Word_Frequency_Counter(Input))
    else:
        # Exit the loop and print a goodbye message when 'stop' is entered
        print('Good by ')
        break
