def transform_input_string():
    # Read input from user and remove unnecessary whitespace
    input_string = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@" in input_string
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Modify the string if it starts with a dot
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Initialize a counter and a list for constructing the output
    counter = 0
    character_list = []

    # Modify the string if it starts with an @
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Iterate through each character in the input string
    for character in input_string:
        # Check for the occurrence of '@'
        if character == "@":
            # Append "at" to character_list if we already encountered an '@'
            if counter > 0:
                character_list.append("at")
            else:
                character_list.append("@")
            counter = 1  # Indicate that we have encountered an '@'
        else:
            # Add the character to character_list if it is not '@'
            character_list.append(character)

    # Join all characters in character_list into a single string
    output_string = ''.join(character_list)

    # Check if the final character is a dot and modify accordingly
    if output_string.endswith("."):
        output_string = output_string[:-1] + "dot"

    # Print the final output
    print(output_string)

# Call the function to execute the transformation
transform_input_string()
