def process_input_string():
    # Step 1: Read a line of input
    input_string = input().strip()  # Removing leading or trailing spaces
    
    # Step 2: Replace words
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check if first character is a period
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string
    
    # Step 4: Initialize counter and list for characters
    at_counter = 0
    character_list = []
    
    # Step 5: Process each character in the modified string
    for character in modified_string:
        if character == "@":
            if at_counter > 0:
                character_list.append("at")
            else:
                character_list.append(character)
                at_counter += 1
        else:
            character_list.append(character)
    
    # Step 6: Join characters into a final string
    final_string = ''.join(character_list)
    
    # Step 7: Check if last character is a period
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"
    
    # Step 8: Output the final modified string
    print(final_string)

# Execute the function
process_input_string()
