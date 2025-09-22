def process_email_format():
    # Step 1: Read Input
    user_input = input().strip()  # Remove leading/trailing whitespace
    
    # Step 2: Replace Keywords
    modified_string = user_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check for Leading Dot
    if modified_string.startswith('.'):
        modified_string = 'dot' + modified_string

    # Step 4: Initialize Variables
    co = 0  # Counter for the appearances of "@" symbol
    processed_chars = []  # List to store processed characters

    # Step 5: Fix the Leading At
    if modified_string.startswith('@'):
        modified_string = 'at' + modified_string

    # Step 6: Process Each Character
    for char in modified_string:
        if char == '@':
            if co > 0:  # If we already have an "@" before
                processed_chars.append('at')
            else:
                processed_chars.append('@')
            co = 1  # Mark that we've seen an "@" 
        else:
            processed_chars.append(char)
            co = 0  # Reset count if it's not "@" 

    # Step 7: Combine Characters
    final_string = ''.join(processed_chars)

    # Step 8: Adjust Trailing Dot
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'  # Replace trailing dot with "dot"

    # Step 9: Output the Result
    print(final_string)

# Call the function to execute the process
process_email_format()
