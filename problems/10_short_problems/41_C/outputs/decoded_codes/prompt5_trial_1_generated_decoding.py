# Function to transform a string representing an email address
def transform_email_address():
    # Step 1: Read the input, removing leading and trailing spaces
    user_input = input().strip()
    
    # Step 2: Initial replacements
    modified_string = user_input.replace('dot', '.').replace('at', '@')
    
    # Step 3: Handle leading character
    if modified_string.startswith('.'):
        modified_string = 'dot' + modified_string[1:]

    # Step 4: Initialize a counter for '@' and a list to hold characters
    at_count = 0
    char_list = []
    
    # Step 5: Handle leading '@'
    if modified_string.startswith('@'):
        modified_string = 'at' + modified_string[1:]

    # Step 6: Iterate over each character in the modified string
    for char in modified_string:
        if char == '@':
            if at_count > 0:
                char_list.append('at')
            else:
                char_list.append('@')
            at_count += 1
        else:
            char_list.append(char)
    
    # Step 7: Join the characters back into a single string
    final_string = ''.join(char_list)
    
    # Step 8: Handle trailing character
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'
    
    # Step 9: Output the final modified string
    print(final_string)

# Example test case
# Input: "john.doe(at)example(dot)com"
# Expected output: "john.dot@at.example.dot.com"
