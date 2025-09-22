def process_email_string():
    # Step 1: Read the input and strip whitespaces
    input_string = input().strip()
    
    # Step 2: Replace terms with appropriate symbols
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle leading character
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Initialize variables
    countAt = 0
    output_list = []

    # Step 5: Check leading character for "at"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process each character
    for char in modified_string:
        if char == "@":
            if countAt > 0:
                output_list.append("at")
                countAt = 1
            else:
                output_list.append("@")
                countAt = 1
        else:
            output_list.append(char)
            
    # Step 7: Join and finalize the output
    final_string = ''.join(output_list)
    
    # If the last character is a ".", replace it with "dot"
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 8: Print the output
    print(final_string)

# Call the function to execute
process_email_string()
