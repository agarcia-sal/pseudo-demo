def process_input_string():
    # Step 1: Read input string and trim whitespace
    input_string = input().strip()
    
    # Step 2: Replace all occurrences of "dot" with "."
    modified_string = input_string.replace("dot", ".")
    
    # Step 3: Replace all occurrences of "at" with "@"
    modified_string = modified_string.replace("at", "@")
    
    # Step 4: Prepend "dot" if the first character is a "."
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string[1:]

    # Step 5: Initialize the counter for '@' 
    consecutive_at_count = 0
    
    # Step 6: Initialize a list to hold processed characters
    processed_characters = []

    # Step 8: Prepend "at" if the first character is "@"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string[1:]

    # Step 9: Process each character in the modified string
    for char in modified_string:
        if char == "@":
            if consecutive_at_count > 0:
                processed_characters.append("at")
            else:
                processed_characters.append("@")
            consecutive_at_count = 1
        else:
            processed_characters.append(char)
            consecutive_at_count = 0

    # Step 10: Join all characters into a single string
    result_string = ''.join(processed_characters)

    # Step 11: Replace the last character with "dot" if it's "."
    if result_string and result_string[-1] == ".":
        result_string = result_string[:-1] + "dot"

    # Step 12: Print the final processed string
    print(result_string)

# Run the function
process_input_string()
