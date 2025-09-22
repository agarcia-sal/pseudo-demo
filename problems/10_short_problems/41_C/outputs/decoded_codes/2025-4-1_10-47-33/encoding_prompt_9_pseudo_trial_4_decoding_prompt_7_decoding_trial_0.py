# Function to transform a given email string by replacing keywords with symbols
def transform_email():
    # Step 1: Receive Input
    email_input = input().strip()  # Read input and remove leading/trailing spaces

    # Step 2: Replace Keywords
    modified_email = email_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check Leading Character
    if modified_email.startswith("."):
        modified_email = "dot" + modified_email[1:]  # Prepend 'dot' if it starts with '.'

    # Step 4: Initialize the List and Counter
    counter = 0  # Counter for occurrences of "at"
    processed_chars = []  # List to collect processed characters

    # Step 5: Check for Leading "at"
    if modified_email.startswith("@"):
        modified_email = "at" + modified_email[1:]  # Prepend 'at' if it starts with '@'

    # Step 6: Process Each Character
    for char in modified_email:
        if char == "@":
            if counter > 0:
                processed_chars.append("at")  # Append 'at' if it's not the first '@'
                counter = 1  # Update counter
            else:
                processed_chars.append(char)  # Append '@' directly
                counter = 1  # Set counter for first occurrence
        else:
            processed_chars.append(char)  # Append other characters directly

    # Step 7: Reconstruct the String
    final_email = ''.join(processed_chars)  # Join list to form the final string

    # Step 8: Check for Trailing Character
    if final_email.endswith("."):
        final_email = final_email[:-1] + "dot"  # Replace trailing '.' with 'dot'

    # Step 9: Output the Result
    print(final_email)  # Print the final processed string

# Call the function to execute
transform_email()
