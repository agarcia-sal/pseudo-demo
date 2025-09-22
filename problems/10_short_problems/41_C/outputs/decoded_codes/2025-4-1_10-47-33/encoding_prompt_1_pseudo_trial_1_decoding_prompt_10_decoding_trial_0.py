def transform_input_string():
    # Read input from the user and strip unnecessary whitespace
    input_string = input().strip()
    
    # Replace all occurrences of "dot" with "." and "at" with "@" 
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Handle case when the input starts with a dot
    if input_string and input_string[0] == '.':
        input_string = "dot" + input_string[1:]

    # Initialize a counter and an empty list for constructing the output
    counter = 0
    character_list = []

    # Handle case when the input starts with an @
    if input_string and input_string[0] == '@':
        input_string = "at" + input_string[1:]

    # Iterate through each character in the input string
    for character in input_string:
        # Check for the occurrence of '@' character
        if character == '@':
            if counter > 0:
                # Append "at" to character_list if we already encountered an '@'
                character_list.append("at")
                counter = 1
            else:
                # Append "@" to character_list for the first occurrence
                character_list.append("@")
                counter = 1
        else:
            # If the character is not '@', simply add it to character_list
            character_list.append(character)

    # Join all characters in character_list into a single string
    output_string = ''.join(character_list)

    # Check if the final character is a dot and modify accordingly
    if output_string and output_string[-1] == '.':
        output_string = output_string[:-1] + "dot"

    # Print the final output
    print(output_string)

# Call the function to execute
transform_input_string()
