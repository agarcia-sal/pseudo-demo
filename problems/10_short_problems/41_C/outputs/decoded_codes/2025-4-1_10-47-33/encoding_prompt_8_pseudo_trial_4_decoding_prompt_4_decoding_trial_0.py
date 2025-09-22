def process_email_format():
    # Step 1: Read Input
    user_input = input().strip()
    
    # Step 2: Replace Specific Words
    modified_input = user_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle Leading Period
    if modified_input.startswith('.'):
        modified_input = "dot" + modified_input[1:]

    # Step 4: Initialize Variables
    at_counter = 0
    processed_chars = []

    # Step 5: Handle Leading At-Symbol
    if modified_input.startswith('@'):
        modified_input = "at" + modified_input[1:]

    # Step 6: Process Each Character
    for char in modified_input:
        if char == '@':
            if at_counter > 0:
                processed_chars.append("at")
                at_counter = 1
            else:
                processed_chars.append(char)
                at_counter = 1
        else:
            processed_chars.append(char)

    # Step 7: Join Characters Together
    result_email = ''.join(processed_chars)
    
    # Step 8: Handle Trailing Period
    if result_email.endswith('.'):
        result_email = result_email[:-1] + "dot"
    
    # Step 9: Output the Result
    print(result_email)

# Call the function to execute the email processing
process_email_format()
