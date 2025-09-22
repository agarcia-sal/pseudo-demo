def transform_email_string():
    # Step 1: Receive Input
    original_string = input().strip()
    
    # Step 2: Replace Word Aliases
    modified_string = original_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust Beginning of String
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string
    
    # Step 4: Initialize Counters and List for Characters
    at_counter = 0
    char_list = []
    
    # Step 5: Handle Special Cases for Starting Character
    if modified_string.startswith("@"):
        char_list.append("at")
        at_counter = 1
    else:
        at_counter = 0  # Set counter only if it starts with "at"
    
    # Step 6: Iterate through Each Character
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                char_list.append("at")
                at_counter += 1  # Increment the counter if we've already seen "at"
            else:
                char_list.append("@")
                at_counter = 1  # Set the counter to 1 since we've now seen "at"
        else:
            char_list.append(char)  # Just append other characters directly
    
    # Step 7: Combine List into String
    final_string = ''.join(char_list)
    
    # Step 8: Adjust End of String
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"
    
    # Step 9: Output Modified String
    print(final_string)

# Run the function
transform_email_string()
