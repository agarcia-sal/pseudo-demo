def process_input():
    # Read a line of input and remove leading/trailing white spaces
    input_line = input().strip()

    # Replace all occurrences of "dot" with "." and "at" with "@"
    updated_string = input_line.replace("dot", ".").replace("at", "@")

    # Check if the first character is "."
    if updated_string and updated_string[0] == ".":
        # Prepend "dot" to the updated_string (excluding the first character)
        updated_string = "dot" + updated_string[1:]

    # Initialize a counter for "at" occurrences and an empty list to store characters
    count_at_symbols = 0
    character_list = []

    # Check if the first character is "@"
    if updated_string and updated_string[0] == "@":
        # Prepend "at" to the updated_string (excluding the first character)
        updated_string = "at" + updated_string[1:]

    # Iterate through each character in the updated_string
    for char in updated_string:
        if char == "@":
            # Check if this is not the first occurrence of "at"
            if count_at_symbols > 0:
                # Append "at" to the character list
                character_list.append("at")
                # Update the counter to indicate "at" has been handled
                count_at_symbols = 1
            else:
                # First occurrence of "@", just append it
                character_list.append("@")
                # Update the counter
                count_at_symbols = 1
        else:
            # For any other character, simply add it to the character list
            character_list.append(char)

    # Join the characters in the list into a single string
    final_string = ''.join(character_list)

    # Check if the last character is "."
    if final_string and final_string[-1] == ".":
        # Replace the last character with "dot"
        final_string = final_string[:-1] + "dot"

    # Output the final modified string
    print(final_string)

# Call the function to process the input
process_input()
