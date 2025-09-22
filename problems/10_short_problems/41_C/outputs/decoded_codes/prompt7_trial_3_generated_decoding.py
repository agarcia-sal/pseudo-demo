def processEmailString():
    # Read the input string and remove leading/trailing whitespace
    emailString = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    emailString = emailString.replace('dot', '.').replace('at', '@')

    # If the email string starts with '.', add 'dot' at the beginning
    if emailString.startswith('.'):
        emailString = 'dot' + emailString[1:]

    # Initialize variables for processing
    occurrenceCounter = 0
    c = []  # List to store processed characters
    length = 0  # Initialize length (not utilized later)

    # If the email string starts with '@', change it to start with 'at'
    if emailString.startswith('@'):
        emailString = 'at' + emailString[1:]

    # Iterate through each character in the email string
    for character in emailString:
        if character == '@':
            # Check if a previous '@' has been encountered
            if occurrenceCounter > 0:
                c.append('at')  # Append "at" for extra '@'
                occurrenceCounter = 1
            else:
                c.append('@')  # Append single '@'
                occurrenceCounter = 1
        else:
            c.append(character)  # Append regular characters

    # Join the list into a single string
    combinedString = ''.join(c)

    # If the last character is '.', replace it with 'dot'
    if combinedString.endswith('.'):
        combinedString = combinedString[:-1] + 'dot'

    # Output the processed email string
    print(combinedString)

# Example usage of the function, to demonstrate the functionality:
# processEmailString()  # Uncomment to test with user input
