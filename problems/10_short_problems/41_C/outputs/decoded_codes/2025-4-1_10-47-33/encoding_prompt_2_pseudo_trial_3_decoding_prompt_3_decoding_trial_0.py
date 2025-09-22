def process_input():
    # Step 1: Read a line of input and remove leading/trailing whitespace
    user_input = input().strip()
    
    # Step 2: Replace "dot" with "."
    modified_input = user_input.replace("dot", ".")
    
    # Step 3: Replace "at" with "@"
    modified_input = modified_input.replace("at", "@")
    
    # Step 4: Check if the first character is a period
    if modified_input.startswith('.'):
        modified_input = 'dot' + modified_input[1:]  # Prepend "dot", excluding the first character

    # Step 5: Initialize counter and list
    at_counter = 0
    char_list = []
    
    # Step 6: Initialize current position (not necessary but included for clarity)
    current_position = 0
    
    # Step 7: Check if first character is "@" and prepend "at"
    if modified_input.startswith('@'):
        modified_input = 'at' + modified_input[1:]  # Prepend "at", excluding the first character
    
    # Step 8: Process each character
    for char in modified_input:
        if char == '@':
            if at_counter > 0:
                char_list.append("at")  # Append "at" if counter is greater than zero
            else:
                char_list.append('@')  # Append "@" if it's our first occurrence
                at_counter = 1  # Set counter
        else:
            char_list.append(char)  # Append the current character

    # Step 9: Join all characters in the list to form a single string
    result_string = ''.join(char_list)

    # Step 10: Check if the last character is a period
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'  # Replace "." with "dot"
    
    # Step 11: Output the modified string
    print(result_string)

# Call the function to run the code
process_input()
