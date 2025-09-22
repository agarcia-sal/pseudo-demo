def transform_email_string():
    # Step 1: Receive Input
    email_string = input().strip()
    
    # Step 2: Replace Word Aliases
    email_string = email_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust Beginning of String
    if email_string.startswith("."):
        email_string = "dot" + email_string
    
    # Step 4: Initialize Counters
    at_counter = 0
    modified_characters = []
    
    # Step 5: Handle Special Cases for Starting Character
    if email_string.startswith("@"):
        modified_characters.append("at")
        at_counter = 1
        # Replace the first character (@) with "at"
        email_string = email_string[1:]  # Remove the "@" to process the rest
    
    # Step 6: Iterate through Each Character
    for char in email_string:
        if char == "@":
            if at_counter > 0:
                modified_characters.append("at")
                at_counter = 1
            else:
                modified_characters.append("@")
                at_counter += 1
        else:
            modified_characters.append(char)
            at_counter = 0  # Reset counter for different characters
    
    # Step 7: Combine List into String
    result_string = ''.join(modified_characters)
    
    # Step 8: Adjust End of String
    if result_string.endswith("."):
        result_string = result_string[:-1] + "dot"
    
    # Step 9: Output Modified String
    print(result_string)

# Call the function to perform the transformation
transform_email_string()
