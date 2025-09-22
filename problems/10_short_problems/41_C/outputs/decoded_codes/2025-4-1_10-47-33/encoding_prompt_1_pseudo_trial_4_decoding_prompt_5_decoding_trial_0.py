# Define the main function to process the input string
def process_string():
    # Step 1: Read input string and trim whitespace
    input_string = input().strip()
    
    # Step 2: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")
    
    # Step 3: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")
    
    # Step 4: Prepend "dot" if the first character is "."
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string[1:]

    # Step 5: Initialize the counter for consecutive "@"
    consecutive_at_count = 0
    
    # Step 6: List to hold processed characters
    processed_characters = []

    # Step 8: Prepend "at" if first character is "@"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string[1:]

    # Step 9: Iterate over each character in the modified string
    for character in modified_string:
        if character == "@":
            if consecutive_at_count > 0:
                # Step 9a.i: Append "at" if "@" has been seen already
                processed_characters.append("at")
                consecutive_at_count = 1
            else:
                # Step 9a.ii: Append "@" for the first occurrence
                processed_characters.append("@")
                consecutive_at_count = 1
        else:
            # Step 9b: Append the current character to the list
            processed_characters.append(character)
            consecutive_at_count = 0  # Reset since the current character is not "@"

    # Step 10: Join the processed characters into a single string
    final_string = ''.join(processed_characters)

    # Step 11: Replace last character with "dot" if it is "."
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"

    # Step 12: Print the final processed string
    print(final_string)

# Call the function to run the program
process_string()
