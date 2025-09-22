def normalize_email_string():
    # Step 1: Read input string
    original_string = input()
    
    # Step 2: Normalize input by replacing specific words with symbols
    modified_string = original_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Ensure the string starts correctly
    if modified_string and modified_string[0] == '.':
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize variables for processing
    at_counter = 0
    c = []  # List to hold characters for final string
    l = 0   # Placeholder for length, not used in the final processing

    # Step 5: Check for "at" at the beginning
    if modified_string and modified_string[0] == '@':
        modified_string = "at" + modified_string[1:]

    # Step 6: Iterate through each character in modified_string
    for character in modified_string:
        if character == '@':
            if at_counter > 0:
                c.append("at")  # Append "at" for continuation
                at_counter += 1
            else:
                c.append("@")  # First occurrence of "at"
                at_counter = 1
        else:
            c.append(character)  # Append non-"at" characters directly

    # Step 7: Construct the final string from list c
    final_string = ''.join(c)

    # Step 8: Adjust if the final string ends with a dot
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the final adjusted string
    print(final_string)

# Example usage
normalize_email_string()
