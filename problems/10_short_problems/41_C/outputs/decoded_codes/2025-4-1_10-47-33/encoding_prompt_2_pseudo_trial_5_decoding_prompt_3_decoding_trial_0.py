def modify_text():
    # Step 1: Read Input
    text = input().strip()  # Obtain a line of text and remove whitespace

    # Step 2: Replace Substrings
    text = text.replace("dot", ".")  # Replace 'dot' with '.'
    text = text.replace("at", "@")    # Replace 'at' with '@'

    # Step 3: Adjust Beginning Character
    if text.startswith('.'):
        text = "dot" + text[1:]  # If it starts with '.', change it to 'dot' followed by the rest

    # Step 4: Initialize Variables
    at_counter = 0  # Counter for occurrences of '@'
    output_chars = []  # List to store final output characters
    length = 0  # To track the length of the text

    # Step 5: Handle Leading '@'
    if text.startswith('@'):
        text = "at" + text[1:]  # If it starts with '@', change it to 'at' followed by the rest

    # Step 6: Iterate Over Each Character
    for char in text:
        if char == '@':
            if at_counter > 0:
                output_chars.append("at")  # Append 'at' for subsequent '@'
            else:
                output_chars.append(char)  # Append '@' for the first occurrence
            at_counter += 1  # Increment the counter for '@'
        else:
            output_chars.append(char)  # Append non-'@' characters directly

    # Step 7: Join Characters
    final_string = ''.join(output_chars)  # Create a single string from the list

    # Step 8: Final Adjustment
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"  # Replace trailing '.' with 'dot'

    # Step 9: Output Result
    print(final_string)  # Display the final modified string

# Execute the function
modify_text()
