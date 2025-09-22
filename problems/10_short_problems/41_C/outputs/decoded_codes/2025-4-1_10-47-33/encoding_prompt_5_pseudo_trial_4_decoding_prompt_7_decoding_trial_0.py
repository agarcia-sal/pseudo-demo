def process_email_string():
    # Read input from the user and strip leading/trailing spaces
    input_string = input().strip()

    # Replace keywords with symbols
    input_string = input_string.replace("dot", ".")  # Replace 'dot' with '.'
    input_string = input_string.replace("at", "@")   # Replace 'at' with '@'

    # If the string starts with a period, prepend "dot"
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]  # Prepend "dot" and exclude the first character

    # Initialize variables for tracking and modification
    count_at_symbol = 0  # Count how many "at" symbols we've processed
    modified_characters = []  # List to hold modified characters

    # If the string starts with "@", prepend "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]  # Prepend "at" and exclude the first character

    # Loop through each character in the modified input string
    for character in input_string:
        # Check if the character is the "at" symbol
        if character == '@':
            # If an "at" symbol has been added before, append 'at' as a word to the list
            if count_at_symbol > 0:
                modified_characters.append("at")  # Append word 'at'
                count_at_symbol = 1  # Reset count
            else:
                modified_characters.append(character)  # Append the "at" symbol
                count_at_symbol = 1  # Update count
        else:
            # If character is not "at", append it to the list
            modified_characters.append(character)

    # Join the modified characters into a single string
    final_string = ''.join(modified_characters)

    # If the final string ends with a period, replace it with "dot"
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"  # Remove the last '.' and append 'dot'

    # Output the final processed string
    print(final_string)

# To execute the function
process_email_string()
