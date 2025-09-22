def convert_to_email_format():
    # Step 1: Read input and trim whitespace
    user_input = input().strip()

    # Step 2: Replace keywords with symbols
    modified_string = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check for leading dot
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string

    # Step 4: Initialize variables for processing
    at_counter = 0  # Counter for appearances of "@"
    processed_chars = []  # List to store processed characters

    # Step 5: Fix the leading at
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string

    # Step 6: Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                processed_chars.append("at")
            else:
                processed_chars.append("@")
            at_counter = 1  # Set the counter to indicate we've seen an "at"
        else:
            processed_chars.append(char)
            at_counter = 0  # Reset counter for any non-"at" character

    # Step 7: Combine characters into a single string
    final_string = ''.join(processed_chars)

    # Step 8: Adjust trailing dot
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the result
    print(final_string)

# Call the function to execute the email conversion
convert_to_email_format()
