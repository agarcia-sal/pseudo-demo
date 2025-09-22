def process_email_string():
    # Step 1: Read input and trim extra spaces
    input_string = input().strip()

    # Step 2: Replace "dot" with "." and "at" with "@"
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Handle leading period
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize a counter for occurrences of "@"
    at_counter = 0
    processed_characters = []

    # Step 5: Handle leading at-symbol
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                processed_characters.append("at")
                at_counter = 1  # Reset counter after processing an "@"
            else:
                processed_characters.append(char)
                at_counter = 1
        else:
            processed_characters.append(char)

    # Step 7: Join characters together into a final string
    final_string = ''.join(processed_characters)

    # Step 8: Handle trailing period
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the result
    print(final_string)

# Call the function to execute
process_email_string()
