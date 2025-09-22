def process_email_string():
    # Read input from the user and strip leading/trailing spaces
    input_string = input().strip()
    
    # Replace specific words with symbols
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # If the string starts with a period, prepend "dot"
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]
    
    # Initialize variables for tracking and modification
    count_at_symbol = 0
    modified_characters = []
    
    # If the string starts with "@", prepend "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Loop through each character in the modified input string
    for character in input_string:
        # Check if the character is the "at" symbol
        if character == '@':
            # If an "at" symbol has been added before
            if count_at_symbol > 0:
                modified_characters.append("at")
                count_at_symbol = 1  # Reset count
            else:
                # If this is the first "at" symbol
                modified_characters.append('@')
                count_at_symbol += 1  # Update count
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

# Test cases (examples):
# Input: "my email is john doe at example dot com"
# Output: "my email is john doe at example.com"
# Input: ".example"
# Output: "dotexample"
# Input: "@user dot com."
# Output: "atuser dot com"
