# Function to process the email-like string input
def process_email_string():
    # Step 1: Read input and strip any leading/trailing whitespace
    input_string = input().strip()
    
    # Step 2: Replace 'dot' and 'at' with '.' and '@' respectively
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Handle leading character if it is '.'
    if modified_string.startswith('.'):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize counter for '@' symbols processed and output list
    countAt = 0
    output_list = []

    # Step 5: Check if the first character is '@'
    if modified_string.startswith('@'):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process each character in the modified string
    for char in modified_string:
        if char == '@':
            if countAt > 0:
                output_list.append("at")
                countAt = 1
            else:
                output_list.append("@")
                countAt = 1
        else:
            output_list.append(char)
    
    # Step 7: Join the output list into a final string
    final_string = ''.join(output_list)

    # Check if final character is '.' and replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 8: Print the modified string
    print(final_string)

# Example usage: Uncomment below to test the function
# process_email_string()
