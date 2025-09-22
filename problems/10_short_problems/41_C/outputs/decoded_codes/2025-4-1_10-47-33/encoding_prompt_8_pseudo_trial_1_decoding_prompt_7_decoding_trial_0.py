# Function to process the email-like string input
def process_email_string():
    # Step 1: Read Input
    input_string = input().strip()  # Get input and remove leading/trailing whitespace

    # Step 2: Replace Terms
    # Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")
    # Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")

    # Step 3: Handle Leading Character
    # If the first character is a '.', prepend "dot"
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize Variables
    countAt = 0  # Counter for "@" symbols
    output_list = []  # List to build the final output

    # Step 5: Check Leading Character for "at"
    # If the first character is '@', change it to "at"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            # If there's already an "@" in our output, append "at" for the next "@"
            if countAt > 0:
                output_list.append("at")
            else:
                output_list.append("@")
                countAt += 1  # Count the first "@" as processed
        else:
            output_list.append(char)

    # Step 7: Join and Finalize Output
    final_string = ''.join(output_list)
    # If the last character is '.', replace it with "dot"
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 8: Print Output
    print(final_string)

# Call the function to execute
process_email_string()
