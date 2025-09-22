# Begin program
def process_string():
    # Step 1: Read input string and strip whitespace
    input_string = input().strip()
    
    # Step 2: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")
    
    # Step 3: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")
    
    # Step 4: Prepend "dot" if the first character is a "."
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string[1:]
    
    # Step 5: Initialize counter for consecutive "@"
    co = 0
    
    # Step 6: Initialize an empty list to hold processed characters
    processed_characters = []
    
    # Step 7: Variable 'l' is not used further in the logic, so we omit it
    
    # Step 8: Prepend "at" if the first character is an "@"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string[1:]
    
    # Step 9: Process the modified string
    for character in modified_string:
        if character == "@":
            if co > 0:  # Step 9a.i
                processed_characters.append("at")
                co = 1
            else:  # Step 9a.ii
                processed_characters.append(character)
                co = 1
        else:  # Step 9b
            processed_characters.append(character)
            co = 0  # Reset the counter if a non-"@" character is encountered

    # Step 10: Join the processed characters into a single string
    final_string = ''.join(processed_characters)
    
    # Step 11: Replace the last character with "dot" if it is "."
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"
    
    # Step 12: Print the final processed string
    print(final_string)

# End program

# Call the function to execute
process_string()
