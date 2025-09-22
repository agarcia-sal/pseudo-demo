def modify_text():
    # Step 1: Read input and remove leading/trailing whitespace
    text = input().strip()

    # Step 2: Replace substrings "dot" with '.' and "at" with '@'
    text = text.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust the beginning character if the text starts with '.'
    if text.startswith('.'):
        text = "dot" + text[1:]

    # Step 4: Initialize variables
    at_counter = 0  # Counter for occurrences of '@'
    output_chars = []  # List to collect characters for output
    text_length = len(text)  # Get the length of the text

    # Step 5: Handle leading '@'
    if text.startswith('@'):
        text = "at" + text[1:]

    # Step 6: Iterate over each character in the modified text
    for char in text:
        if char == '@':
            if at_counter > 0:  # If this is not the first '@'
                output_chars.append("at")
            else:  # First '@' encountered
                output_chars.append(char)
            at_counter += 1
        else:
            output_chars.append(char)

    # Step 7: Join characters to form the final output string
    final_output = ''.join(output_chars)

    # Step 8: Final adjustment if the last character is '.'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + "dot"

    # Step 9: Display the final modified string
    print(final_output)

# Run the function to modify the input text
modify_text()
