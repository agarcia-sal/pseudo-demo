# Initialize the function to process the input string for email formatting
def format_email():
    # 1. Read input from the user
    user_input = input().strip()  # Remove leading/trailing whitespace

    # 2. Replace occurrences of 'dot' with '.' and 'at' with '@'
    modified_string = user_input.replace("dot", ".").replace("at", "@")

    # 3. Check for leading dot
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string

    # 4. Initialize variables
    co = 0  # Counter for the '@' symbol
    c = []  # List to store processed characters
    l = 0   # This variable is initialized but not used

    # 5. Fix the leading '@'
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string

    # 6. Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if co > 0:
                c.append("at")  # Append 'at' if '@' has appeared before
                co = 1  # Reset counter to 1
            else:
                c.append("@")  # Append '@' to the list
                co = 1  # Increment counter
        else:
            c.append(char)  # Append any other character

    # 7. Combine characters into a single string
    final_string = ''.join(c)

    # 8. Adjust trailing dot
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # 9. Output the result
    print(final_string)

# Call the function to execute
format_email()
