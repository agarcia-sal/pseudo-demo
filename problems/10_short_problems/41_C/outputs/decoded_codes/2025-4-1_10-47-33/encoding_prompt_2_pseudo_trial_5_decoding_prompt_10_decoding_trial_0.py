def process_text():
    # Step 1: Read Input
    text_input = input().strip()

    # Step 2: Replace substrings
    modified_text = text_input.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust beginning character
    if modified_text.startswith('.'):
        modified_text = "dot" + modified_text[1:]

    # Step 4: Initialize Variables
    at_counter = 0
    result_characters = []
    
    # Step 5: Handle Leading '@'
    if modified_text.startswith('@'):
        modified_text = "at" + modified_text[1:]

    # Step 6: Iterate Over Each Character
    for char in modified_text:
        if char == '@':
            if at_counter > 0:  # If this is not the first '@'
                result_characters.append("at")
            else:  # If this is the first '@'
                result_characters.append('@')
            at_counter += 1
        else:
            result_characters.append(char)

    # Step 7: Join Characters
    final_output = ''.join(result_characters)

    # Step 8: Final Adjustment
    if final_output.endswith('.'):
        final_output = final_output[:-1] + "dot"

    # Step 9: Output Result
    print(final_output)

# Call the function to execute the process
process_text()
