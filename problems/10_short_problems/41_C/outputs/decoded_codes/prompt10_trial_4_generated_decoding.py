def process_input():
    # Step 1: Read input
    input_string = input().strip()

    # Step 2: Replace keywords with respective symbols
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # Step 3: Ensure a leading "dot" if the string starts with a "."
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize variables for processing
    counter_at = 0  # Counter for occurrences of '@'
    character_list = []  # List to store processed characters

    # Step 5: Check for leading "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Step 6: Process each character in input_string
    for character in input_string:
        if character == "@":
            if counter_at > 0:
                character_list.append("at")
                counter_at = 1
            else:
                character_list.append("@")
                counter_at = 1
        else:
            character_list.append(character)

    # Step 7: Join the list character_list into a string
    processed_string = ''.join(character_list)

    # Step 8: Replace a trailing dot with "dot"
    if processed_string.endswith('.'):
        processed_string = processed_string[:-1] + "dot"

    # Step 9: Output the final modified string
    print(processed_string)

# Call the function to execute
process_input()
