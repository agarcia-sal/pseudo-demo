# Function to convert a non-standard email format to a standard email format
def convert_email_format():
    # Read input and remove extra spaces around it
    input_string = input().strip()
    
    # Replace specific words with their corresponding characters
    modified_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Handle leading period by replacing it with "dot"
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]
    
    # Initialize counter for '@' occurrences and an empty list for processed characters
    at_counter = 0
    processed_characters = []
    
    # Handle leading at-symbol by replacing it with "at" if present at the beginning
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]
    
    # Process each character in the modified string
    for character in modified_string:
        if character == "@":
            if at_counter > 0:
                # Append "at" to the list if we've already processed an '@'
                processed_characters.append("at")
                # Reset the counter after processing
                at_counter = 1
            else:
                # Append the '@' to the list
                processed_characters.append(character)
                at_counter = 1
        else:
            # Append characters that are not '@'
            processed_characters.append(character)
    
    # Join characters together into a single string
    final_result = ''.join(processed_characters)
    
    # Handle trailing period by replacing it with "dot"
    if final_result.endswith("."):
        final_result = final_result[:-1] + "dot"
    
    # Output the final processed string
    print(final_result)

# Uncomment the following line to run the function
# convert_email_format()
