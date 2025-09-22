def format_email_string():
    # Read a line of text from the user and remove any extra spaces
    input_string = input().strip()
    
    # Step 1: Replace all occurrences of "dot" with a period (.)
    formatted_string = input_string.replace("dot", ".")
    
    # Step 2: Replace all occurrences of "at" with the symbol (@)
    formatted_string = formatted_string.replace("at", "@")
    
    # Step 3: Check if the first character of the string is a period
    if formatted_string.startswith('.'):
        # Prepend "dot" to the remaining part of the string
        formatted_string = "dot" + formatted_string[1:]

    # Step 4: Initialize a counter for "at" symbols as zero
    at_counter = 0
    # Create an empty list to hold characters
    char_list = []
    
    # Step 5: Check if the first character of the formatted string is an "at" symbol
    if formatted_string.startswith('@'):
        # Prepend "at" to the remaining part of the string
        formatted_string = "at" + formatted_string[1:]

    # Step 6: Loop through each character in the string
    for char in formatted_string:
        if char == '@':
            if at_counter > 0:
                # Add "at" to the list if counter is greater than 0
                char_list.append("at")
                at_counter = 1  # Reset the counter
            else:
                # Add the "at" symbol to the list
                char_list.append('@')
                at_counter = 1
        else:
            # Add the character to the list
            char_list.append(char)

    # Step 7: Join all characters in the list into a single string
    final_string = ''.join(char_list)
    
    # Step 8: Check if the last character of the final string is a period
    if final_string.endswith('.'):
        # Replace the period with "dot"
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the final formatted string to the user
    print(final_string)

# Example of how to run the function
# format_email_string()  # Uncomment to use it interactively
