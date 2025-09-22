def transform_email():
    # Step 1: Receive Input
    email_input = input().strip()
    
    # Step 2: Replace Keywords
    email_input = email_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check Leading Character
    if email_input.startswith('.'):
        email_input = "dot" + email_input[1:]
    
    # Step 4: Initialize the List and Counter
    at_counter = 0
    processed_chars = []
    
    # Step 5: Check for Leading "at"
    if email_input.startswith('@'):
        email_input = "at" + email_input[1:]
    
    # Step 6: Process Each Character
    for char in email_input:
        if char == '@':
            if at_counter > 0:
                processed_chars.append("at")
            else:
                processed_chars.append(char)
            at_counter = 1  # increment the counter when we encounter '@'
        else:
            processed_chars.append(char)
            at_counter = 0  # reset the counter for any other character
    
    # Step 7: Reconstruct the String
    final_email = ''.join(processed_chars)
    
    # Step 8: Check for Trailing Character
    if final_email.endswith('.'):
        final_email = final_email[:-1] + "dot"  # replace last '.' with 'dot'
    
    # Step 9: Output the Result
    print(final_email)

# Execute the function
transform_email()
