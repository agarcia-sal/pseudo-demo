def process_email_string():
    # Step 1: Read Input
    input_string = input().strip()

    # Step 2: Replace Terms
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle Leading Character
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize Variables
    countAt = 0
    output_list = []
    
    # Step 5: Check Leading Character for "at"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            if countAt > 0:
                output_list.append("at")
            else:
                output_list.append("@")
                countAt = 1
        else:
            output_list.append(char)

    # Step 7: Join and Finalize Output
    final_string = ''.join(output_list)
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 8: Print Output
    print(final_string)

# Call the function to execute the email processing
process_email_string()
