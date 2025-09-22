# Function to convert a specific input string into an email format
def format_email():
    # Step 1: Receive input and remove surrounding whitespace
    input_string = input().strip()
    
    # Step 2: Replace keywords with symbols
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check for leading dot and prepend "dot" if necessary
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]
    
    # Initialize variables
    count = 0
    char_list = []
    
    # Step 5: Check for leading "at" and prepend "at" if necessary
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]
    
    # Step 6: Process each character in the modified string
    for character in input_string:
        if character == "@":
            if count > 0:
                # If "at" was added before, add it again
                char_list.append("at")
                count = 1
            else:
                # Add "@" symbol
                char_list.append("@")
                count = 1
        else:
            char_list.append(character)
    
    # Step 7: Reconstruct the string
    final_string = ''.join(char_list)
    
    # Step 8: Check for trailing dot and modify accordingly
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"
    
    # Step 9: Output the final formatted string
    print(final_string)

# Example usage:
# format_email()  # The user can call this function to run the email formatting
