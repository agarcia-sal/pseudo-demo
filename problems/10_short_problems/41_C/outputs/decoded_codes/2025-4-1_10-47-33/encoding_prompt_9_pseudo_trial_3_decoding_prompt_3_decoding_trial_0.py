def transform_email_string():
    # Step 1: Receive input and remove surrounding whitespace
    input_string = input().strip()
    
    # Step 2: Replace text patterns
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust leading character
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string
    
    # Step 4: Initialize variables
    at_counter = 0
    character_list = []
    
    # Step 5: Check for leading "at"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string
    
    # Step 6: Iterate through each character in the modified string
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                character_list.append("at")
                at_counter = 1
            else:
                character_list.append("@")
                at_counter = 1
        else:
            character_list.append(char)
            at_counter = 0
    
    # Step 7: Reconstruct the string
    result_string = ''.join(character_list)
    
    # Step 8: Adjust trailing character
    if result_string and result_string[-1] == ".":
        result_string = result_string[:-1] + "dot"
    
    # Step 9: Output the result
    print(result_string)

# To test the function, you can call it directly
transform_email_string()
