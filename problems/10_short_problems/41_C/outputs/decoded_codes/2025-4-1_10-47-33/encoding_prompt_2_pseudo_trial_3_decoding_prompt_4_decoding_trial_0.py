def transform_string():
    # Step 1: Read input line and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Step 2: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")
    
    # Step 3: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")
    
    # Step 4: Check if first character is ".", prepend "dot" if true
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string[1:]
    
    # Step 5: Initialize counter for occurrences of "@" and a character list
    at_counter = 0
    char_list = []
    
    # Step 6: Current position variable (not explicitly used in logic)
    current_position = 0
    
    # Step 7: Check if the first character is "@", prepend "at" if true
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string[1:]
    
    # Step 8: Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                char_list.append("at")
                at_counter = 1
            else:
                char_list.append("@")
                at_counter = 1
        else:
            char_list.append(char)
    
    # Step 9: Join all elements in the list to form a single string
    final_string = ''.join(char_list)
    
    # Step 10: Check if last character is ".", replace it with "dot" if true
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"
    
    # Output the modified string
    print(final_string)

# Call the function to execute
transform_string()
