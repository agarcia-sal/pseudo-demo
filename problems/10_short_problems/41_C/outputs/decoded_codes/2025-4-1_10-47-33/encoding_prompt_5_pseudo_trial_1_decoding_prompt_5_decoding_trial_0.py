# Function to convert specific text into an email-like format
def convert_to_email_format():
    # Step 1: Read input and remove whitespace
    user_input = input().strip()
    
    # Step 2: Replace 'dot' with '.' and 'at' with '@'
    modified_string = user_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check for leading dot
    if modified_string.startswith('.'):
        modified_string = "dot" + modified_string
        
    # Step 4: Initialize counter and list
    appearance_count = 0  # To track occurrences of '@'
    processed_characters = []  # To store processed characters
    unused_variable = 0  # Unused based on pseudocode
    
    # Step 5: Fix leading at
    if modified_string.startswith('@'):
        modified_string = "at" + modified_string
        
    # Step 6: Process each character in the modified string
    for char in modified_string:
        if char == '@':
            # Handle multiple '@' symbols
            if appearance_count > 0:
                processed_characters.append("at")
                appearance_count = 1  # Reset because '@' has appeared again
            else:
                processed_characters.append("@")
                appearance_count = 1  # Set to indicate the presence of an '@'
        else:
            # For characters other than '@', just append them
            processed_characters.append(char)

    # Step 7: Combine processed characters into a single string
    final_string = ''.join(processed_characters)
    
    # Step 8: Adjust trailing dot
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"
    
    # Step 9: Output the result
    print(final_string)

# Example usage scenario in comments
# Input: "example dot com at user"
# Output: "example.com@user"
