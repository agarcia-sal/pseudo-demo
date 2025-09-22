def transform_input_string():
    # Step 1: Receive Input
    user_input = input().strip()

    # Step 2: Replace Keywords
    modified_string = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check for Leading Symbols
    if modified_string.startswith('.'):
        modified_string = "dot" + modified_string

    # Step 4: Initialize Variables
    at_counter = 0
    characters_list = []
    length = 0

    # Step 5: Check for Leading "at"
    if modified_string.startswith('@'):
        modified_string = "at" + modified_string

    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                characters_list.append("at")
            else:
                characters_list.append("@")
                at_counter += 1
        else:
            characters_list.append(char)

    # Step 7: Join Characters
    final_string = ''.join(characters_list)

    # Step 8: Check Trailing Symbols
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the Result
    print(final_string)

# Example call to the function
transform_input_string()
