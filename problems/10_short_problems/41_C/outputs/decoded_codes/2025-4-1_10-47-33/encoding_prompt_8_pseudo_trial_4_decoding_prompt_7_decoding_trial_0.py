# Function to convert a non-standard email address format to a standard format
def convert_email_format():
    # Step 1: Read Input
    user_input = input().strip()  # Get the input and remove surrounding spaces

    # Step 2: Replace Specific Words
    modified_string = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Handle Leading Period
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]  # Replace leading period with "dot"

    # Initialize Variables
    at_counter = 0  # Counter to track occurrences of '@'
    processed_chars = []  # List to hold processed characters

    # Step 5: Handle Leading At-Symbol
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]  # Replace leading '@' with "at"

    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            if at_counter > 0:  # If we've already processed an '@'
                processed_chars.append("at")  # Replace with "at"
                at_counter = 1  # Reset the counter
            else:
                processed_chars.append("@")  # Append the '@'
                at_counter = 1  # Increment counter
        else:
            processed_chars.append(char)  # Append non-@ character

    # Step 7: Join Characters Together
    final_string = ''.join(processed_chars)  # Combine the list into a string

    # Step 8: Handle Trailing Period
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace trailing period with "dot"

    # Step 9: Output the Result
    print(final_string)  # Print the final processed string

# Call the conversion function
convert_email_format()
