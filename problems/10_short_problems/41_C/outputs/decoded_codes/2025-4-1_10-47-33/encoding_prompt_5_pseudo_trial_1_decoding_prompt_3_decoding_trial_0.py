def format_email_input():
    # Step 1: Read input and strip whitespace
    user_input = input().strip()

    # Step 2: Replace keywords with symbols
    modified_input = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check for leading dot
    if modified_input and modified_input[0] == '.':
        modified_input = "dot" + modified_input

    # Step 4: Initialize variables
    co = 0  # Counter for "@" appearences
    processed_chars = []  # List to store processed characters

    # Step 5: Fix the leading "at"
    if modified_input and modified_input[0] == '@':
        modified_input = "at" + modified_input

    # Step 6: Process each character
    for char in modified_input:
        if char == '@':
            if co > 0:
                processed_chars.append("at")  # Append "at" if "@" appeared before
                co = 1  # Reset counter to 1 since we encountered another "@"
            else:
                processed_chars.append("@")  # First appearance of "@"
                co = 1  # First appearance counter
        else:
            processed_chars.append(char)  # Append other characters

    # Step 7: Combine characters into a single string
    final_string = ''.join(processed_chars)

    # Step 8: Adjust trailing dot
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + "dot"  # Replace trailing dot with "dot"

    # Step 9: Output the result
    print(final_string)

# To execute the function
format_email_input()
