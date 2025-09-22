def process_input_string():
    # Read input from standard input and remove leading/trailing whitespace
    input_string = input().strip()

    # Replace occurrences of substrings
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # If the string starts with a ".", prepend "dot" to the string
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Initialize variables for processing
    count_at_symbols = 0
    character_storage = []
    
    # If the string starts with "@", prepend "at" to the string
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Process each character in the input_string
    for character in input_string:
        if character == "@":
            if count_at_symbols > 0:
                character_storage.append("at")
            else:
                character_storage.append("@")
            count_at_symbols += 1
        else:
            character_storage.append(character)

    # Join the list of characters into a single string
    processed_string = ''.join(character_storage)

    # If the string ends with ".", replace it with "dot"
    if processed_string.endswith("."):
        processed_string = processed_string[:-1] + "dot"

    # Output the final processed string
    print(processed_string)

# Call the function to execute the logic
process_input_string()
