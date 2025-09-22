def transform_email_string():
    # Step 1: Receive Input
    user_input = input().strip()
    
    # Step 2: Replace Word Aliases
    modified_string = user_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust Beginning of String
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string
    
    # Step 4: Initialize Counters
    at_counter = 0  # Counter for the occurrence of "@"
    characters_list = []  # List to store characters of the modified string

    # Step 5: Handle Special Cases for Starting Character
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Iterate through Each Character
    for char in modified_string:
        if char == "@":
            if at_counter > 0:  # If we already added an "at"
                characters_list.append("at")
                at_counter = 1  # Reset counter
            else:
                characters_list.append("@")
                at_counter = 1  # Increment counter
        else:
            characters_list.append(char)  # Append the current character

    # Step 7: Combine List into String
    result_string = ''.join(characters_list)

    # Step 8: Adjust End of String
    if result_string.endswith("."):
        result_string = result_string[:-1] + "dot"  # Replace last '.' with 'dot'

    # Step 9: Output Modified String
    print(result_string)

# Test case example (uncomment to test)
# Transform email-like string: transform_email_string()
