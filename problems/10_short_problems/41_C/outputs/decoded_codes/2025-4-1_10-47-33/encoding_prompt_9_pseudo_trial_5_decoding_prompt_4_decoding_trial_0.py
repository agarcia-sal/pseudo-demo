def transform_input_string():
    # 1. Receive Input
    input_string = input().strip()

    # 2. Replace Keywords
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # 3. Check for Leading Symbols
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string

    # 4. Initialize Variables
    at_counter = 0
    characters = []  # list to hold characters
    length = len(modified_string)

    # 5. Check for Leading "at"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string

    # 6. Process Each Character
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                characters.append("at")
            else:
                characters.append("@")
            at_counter += 1  # Increment the counter when '@' is found
        else:
            characters.append(char)

    # 7. Join Characters
    final_string = ''.join(characters)

    # 8. Check Trailing Symbols
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"

    # 9. Output the Result
    print(final_string)

# Call the function to execute the transformation
transform_input_string()
