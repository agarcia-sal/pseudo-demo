def modify_text():
    # Read a line of input and trim whitespace
    input_text = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    modified_text = input_text.replace("dot", ".").replace("at", "@")

    # Adjust starting character if it begins with a '.'
    if modified_text.startswith('.'):
        modified_text = "dot" + modified_text[1:]

    # Initialize variables to track occurrences and collect final characters
    at_counter = 0
    final_chars = []
    
    # Handle leading '@' if present
    if modified_text.startswith('@'):
        final_chars.append("at")
        at_counter += 1
        modified_text = modified_text[1:]

    # Iterate over each character in the modified string
    for char in modified_text:
        if char == '@':
            if at_counter > 0:
                final_chars.append("at")
            final_chars.append('@')
            at_counter += 1
        else:
            final_chars.append(char)

    # Join the list of characters into a single string
    final_output = ''.join(final_chars)

    # Final adjustment: if the last character is '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + "dot"

    # Print the final modified string
    print(final_output)

# Example test cases (uncomment to run):
# print(modify_text("Welcome to the dot com domain."))
# print(modify_text("Please send your queries at support@service.com."))
# print(modify_text("at@domain.comdot"))
