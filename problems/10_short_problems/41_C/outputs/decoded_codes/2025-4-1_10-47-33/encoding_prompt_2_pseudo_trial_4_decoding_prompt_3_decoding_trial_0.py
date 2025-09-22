def modify_string():
    # Step 1: Read a line of input
    input_string = input().strip() # Step 2: Remove leading/trailing spaces

    # Step 3: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")

    # Step 4: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")

    # Step 5: Check if the first character is a period
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string

    # Step 6: Initialize a counter for "@" occurrences and character list
    at_counter = 0
    result_chars = []
    
    # Step 7: Track the length of the string (not used further)
    length_of_string = len(modified_string)

    # Step 8: Check if the first character is "@"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string

    # Step 9: Iterate through characters in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:  # If "@" has been added before
                result_chars.append("at")
            else:
                result_chars.append("@")
                at_counter += 1  # Increment counter
        else:
            result_chars.append(char)

    # Step 10: Join characters into a final result string
    final_string = ''.join(result_chars)

    # Step 11: Check if the last character of the final string is a period
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 12: Output the final modified string
    print(final_string)

# Call the function
modify_string()
