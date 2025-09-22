def transform_email_string():
    # Step 1: Receive Input
    email_string = input().strip()
    
    # Step 2: Replace Text Patterns
    email_string = email_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust Leading Character
    if email_string and email_string[0] == ".":
        email_string = "dot" + email_string
    
    # Step 4: Initialize Variables
    at_counter = 0
    output_characters = []
    
    # Step 5: Check for Leading "at"
    if email_string and email_string[0] == "@":
        email_string = "at" + email_string
        
    # Step 6: Iterate Through Each Character
    for char in email_string:
        if char == "@":
            if at_counter > 0:
                output_characters.append("at")
                at_counter = 1  # Reset counter as we have added "at"
            else:
                output_characters.append(char)
                at_counter = 1  # Set counter when first "@" is appended
        else:
            output_characters.append(char)
            at_counter = 0  # Reset counter for non-"@" characters
    
    # Step 7: Reconstruct the String
    transformed_string = ''.join(output_characters)
    
    # Step 8: Adjust Trailing Character
    if transformed_string and transformed_string[-1] == ".":
        transformed_string = transformed_string[:-1] + "dot"
    
    # Step 9: Output the Result
    print(transformed_string)

# Example of calling the function
transform_email_string()
