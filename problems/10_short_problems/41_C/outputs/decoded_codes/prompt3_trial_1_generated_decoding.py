def process_input():
    # Read a line of input from the user
    user_input = input().strip()
    
    # Replace occurrences of "dot" with a "." in the input
    user_input = user_input.replace("dot", ".")
    
    # Replace occurrences of "at" with "@" in the input
    user_input = user_input.replace("at", "@")
    
    # If the input starts with a ".", prepend "dot" to it
    if user_input.startswith("."):
        user_input = "dot" + user_input[1:]

    # Initialize a counter and an empty list to store characters
    counter = 0
    character_list = []
    
    # If the input starts with "@", prepend "at" to it
    if user_input.startswith("@"):
        user_input = "at" + user_input[1:]

    # Iterate through each character in the modified input
    for character in user_input:
        if character == "@":
            if counter > 0:
                # If this is not the first "at", append "at" to the list
                character_list.append("at")
            else:
                # This is the first "at", append the "@" character to the list
                character_list.append("@")
                counter += 1
        else:
            # Append the current character to the list
            character_list.append(character)

    # Join the character list into a single string
    modified_string = ''.join(character_list)

    # If the modified string ends with a ".", replace it with "dot"
    if modified_string.endswith("."):
        modified_string = modified_string[:-1] + "dot"

    # Output the final modified string
    print(modified_string)

# Call the function to execute
process_input()
