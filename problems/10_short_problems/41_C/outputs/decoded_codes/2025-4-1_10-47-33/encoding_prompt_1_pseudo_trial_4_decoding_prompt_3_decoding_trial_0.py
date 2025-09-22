def process_string():
    # Step 1: Read input and strip leading/trailing whitespace
    input_string = input().strip()
    
    # Step 2: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")
    
    # Step 3: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")
    
    # Step 4: Prepend "dot" if the first character is "."
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]
    
    # Step 5: Initialize consecutive "@" counter and a list for processed characters
    co = 0
    processed_chars = []
    
    # Step 6: "l" initialized but not used
    
    # Step 8: Prepend "at" if the first character is "@"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]
    
    # Step 9: Process each character in modified string
    for character in modified_string:
        if character == "@":
            if co > 0:  # If "@" has been seen before
                processed_chars.append("at")
                co = 1
            else:
                processed_chars.append("@")
                co = 1
        else:
            processed_chars.append(character)
            co = 0  # Reset the counter when a non-"@" character is encountered
    
    # Step 10: Join characters into a final string
    final_string = ''.join(processed_chars)
    
    # Step 11: Replace last character with "dot" if it is "."
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"
    
    # Step 12: Print the final processed string
    print(final_string)

# Example of how to call the function
process_string()
