# Function to modify a given input string according to specific rules
def modify_string():
    # Read input string and remove leading/trailing spaces
    input_string = input().strip()
    
    # Replace specific words with desired characters
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Check if the first character is a period
    if modified_string.startswith('.'):
        modified_string = "dot" + modified_string
    
    # Initialize counter for occurrences of "@" and an empty list for characters
    at_counter = 0
    modified_list = []
    
    # Length of string (not actively used further)
    string_length = len(modified_string)
    
    # Check if the first character is "@"
    if modified_string.startswith('@'):
        modified_string = "at" + modified_string[1:]
    
    # Iterate through each character in the modified string
    for char in modified_string:
        if char == '@':
            if at_counter > 0:
                modified_list.append("at")  # Append "at" if "@" has been added before
            else:
                modified_list.append("@")  # Append "@" for the first occurrence
                at_counter += 1  # Increase the counter for "@" added
        else:
            modified_list.append(char)  # Append non-"@" characters
    
    # Join the modified list into a single string
    final_string = ''.join(modified_list)
    
    # Check if the last character is a period
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"  # Replace period with "dot"
    
    # Output the final modified string
    print(final_string)

# To test the function, you can call modify_string() after defining it
