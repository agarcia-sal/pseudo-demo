def transform_email_string():
    # Step 1: Receive Input
    input_string = input().strip()

    # Step 2: Replace Text Patterns
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust Leading Character
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string

    # Step 4: Initialize Variables
    at_counter = 0
    result_characters = []

    # Step 5: Check for Leading "at"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string

    # Step 6: Iterate Through Each Character
    for character in modified_string:
        if character == "@":
            if at_counter > 0:
                result_characters.append("at")  # Append "at" instead of additional "@" 
            else:
                result_characters.append("@")    # Append the "@" character once
            at_counter += 1  # Increment the counter
        else:
            result_characters.append(character)  # Append the character if not "@"
            at_counter = 0  # Reset counter for non-"@" characters

    # Step 7: Reconstruct the String
    final_string = ''.join(result_characters)

    # Step 8: Adjust Trailing Character
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace trailing "." with "dot"

    # Step 9: Output the Result
    print(final_string)
