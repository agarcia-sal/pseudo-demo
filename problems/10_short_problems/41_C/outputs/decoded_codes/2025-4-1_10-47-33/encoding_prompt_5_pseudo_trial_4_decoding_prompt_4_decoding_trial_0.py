def process_email_string():
    # Read input from the user and remove leading/trailing spaces
    input_string = input().strip()

    # Replace specific words with symbols
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # Initialize variables for tracking and modification
    count_at_symbol = 0
    modified_characters = []
    
    # Check if the string starts with a period, prepend "dot" if it does
    if input_string.startswith('.'):
        modified_characters.append("dot")
        input_string = input_string[1:]  # Exclude the first character

    # Check if the string starts with "@", prepend "at" if it does
    if input_string.startswith('@'):
        modified_characters.append("at")
        input_string = input_string[1:]  # Exclude the first character

    # Loop through each character in the modified input string
    for character in input_string:
        # Check if the character is the "at" symbol
        if character == '@':
            # If an "at" symbol has been added before
            if count_at_symbol > 0:
                modified_characters.append("at")
            else:
                modified_characters.append(character)
                
            count_at_symbol += 1  # Increment count
        else:
            # If character is not "at", append it to the list
            modified_characters.append(character)

    # Join the modified characters into a single string
    final_string = ''.join(modified_characters)

    # If the final string ends with a period, replace it with "dot"
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Output the final processed string
    print(final_string)

# Run the function to process the email-like string
process_email_string()
