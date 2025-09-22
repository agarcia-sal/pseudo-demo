def convert_email_format():
    # Step 1: Read Input
    user_input = input().strip()
    
    # Step 2: Replace Specific Words
    modified_input = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Handle Leading Period
    if modified_input.startswith("."):
        modified_input = "dot" + modified_input[1:]

    # Step 4: Initialize Variables
    at_count = 0
    processed_characters = []

    # Step 5: Handle Leading At-Symbol
    if modified_input.startswith("@"):
        modified_input = "at" + modified_input[1:]

    # Step 6: Process Each Character
    for character in modified_input:
        if character == "@":
            if at_count > 0:
                processed_characters.append("at")
                at_count = 1
            else:
                processed_characters.append(character)
                at_count += 1
        else:
            processed_characters.append(character)

    # Step 7: Join Characters Together
    result_string = ''.join(processed_characters)

    # Step 8: Handle Trailing Period
    if result_string.endswith("."):
        result_string = result_string[:-1] + "dot"

    # Step 9: Output the Result
    print(result_string)

# Call the function to execute
convert_email_format()
