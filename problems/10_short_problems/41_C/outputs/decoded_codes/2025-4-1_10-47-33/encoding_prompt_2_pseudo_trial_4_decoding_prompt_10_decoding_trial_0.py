def process_input_string():
    # Step 1: Read the input string
    input_string = input().strip()  # Remove leading and trailing spaces

    # Step 3: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")

    # Step 4: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")

    # Step 5: Check if the first character is "."
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string  # Add "dot" to the start

    # Step 6: Initialize counter and list for characters
    at_counter = 0
    result_characters = []

    # (Step 7 is omitted as length is not used further)

    # Step 8: Check if the first character is "@"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]  # Replace "@" at the start with "at"

    # Step 9: Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                result_characters.append("at")  # Append "at" if "@" was added before
            else:
                result_characters.append("@")  # Append "@" and increment counter
                at_counter += 1
        else:
            result_characters.append(char)  # Append other characters as they are

    # Step 10: Join characters into a final string
    final_result = ''.join(result_characters)

    # Step 11: Check if the last character of the final string is "."
    if final_result.endswith("."):
        final_result = final_result[:-1] + "dot"  # Replace "." at the end with "dot"

    # Step 12: Output the final modified string
    print(final_result)

# Call the function to execute
process_input_string()
